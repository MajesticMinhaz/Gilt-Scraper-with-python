def scraper(product_url: str, serial_number: int) -> None:
    driver.switch_to.window(driver.window_handles[serial_number % 2])
    driver.get(product_url)
    driver.implicitly_wait(2.5)
    try:
        soup = BeautifulSoup(markup=driver.page_source, features='html.parser')
        script_tags = soup.find_all(name="script")

        json_value_tags = list(filter(lambda script_tag: re.findall(basic_data_matcher_condition, script_tag.text.strip()), script_tags))

        json_value = loads(re.search(pattern=r"{.*}", string=str(json_value_tags[0])).group().strip())

        handle_text = f"gilt_{json_value.get('product_context_id')}"
        title = json_value.get("name")
        vendor = json_value.get("brand")
        price_text = json_value.get("list_price_min")
        custom_product_type = json_value.get("name")
        body_html = json_value.get("skus")[0]["features"]

        available_sizes = []
        available_colors = ["One Color"]

        if json_value.get("sizes") is not None:
            for size in json_value.get("sizes"):
                available_sizes.append(size.get("display_value"))
        else:
            pass

        images_url = []
        style_tag = soup.find(name="style").text.strip()
        img_urls = re.findall(pattern=r"//(.+_([\d+]).[a-z]+)", string=style_tag)

        current_image_number = ""
        for _url in img_urls:
            if _url[1] != current_image_number:
                current_image_number = _url[1]
                images_url.append(_url[0])
            else:
                continue

        sizes = []
        for size in available_sizes:
            # for _ in available_colors:
            sizes.append(size)

        if len(available_colors) != 0 and len(available_sizes) != 0:
            colors = available_colors * len(available_sizes)
        elif len(available_colors) == 0 and len(available_sizes) != 0:
            colors = ['One Color'] * len(available_sizes)
        elif len(available_colors) != 0 and len(available_sizes) == 0:
            colors = available_colors
        else:
            colors = ["No Color"]

        price = [price_text for _ in colors]
        image_position = [str(number) for number in range(1, len(images_url) + 1)]
        variant_image = [images_url[0]]

        json_tag_value_tag = list(filter(lambda script_tag: re.findall(r"var utag_data = (.*);", script_tag.text.strip()), script_tags))
        json_tag_value = loads(re.search(pattern=r"var utag_data = (.*);", string=str(json_tag_value_tag[0])).group(1).strip())

        tags = ""
        for division in json_tag_value.get("product_division"):
            if division is not None:
                tags += division if len(tags).__eq__(0) else f", {division}"
            else:
                continue

        for department in json_tag_value.get("product_department"):
            if department is not None:
                tags += department if len(tags).__eq__(0) else f", {department}"
            else:
                continue

        for product_class in json_tag_value.get("product_class"):
            if product_class is not None:
                tags += product_class if len(tags).__eq__(0) else f", {product_class}"
            else:
                continue

        for product_subclass in json_tag_value.get("product_subclass"):
            if product_subclass is not None:
                tags += product_subclass if len(tags).__eq__(0) else f", {product_subclass}"
            else:
                continue

        json_template = JsonTemplate(
            handle_text=handle_text,
            title=title,
            body_html=body_html,
            vendor=vendor,
            custom_product_type=custom_product_type,
            tags=tags,
            product_id=product_url,
            colors=colors,
            sizes=sizes,
            price=price,
            image_src=images_url,
            image_position=image_position,
            variant_image=variant_image
        )

        my_data = json_template.main_dict()

        if not db.contains(query.ID.any(query.value == str(product_url))):
            db.insert(my_data)
            url_db.remove(query.product_url == product_url)
            print(f"Completely Scraped {product_url}")
        else:
            url_db.remove(query.product_url == product_url)
            print(f"This product already exists : {product_url}")
    except Exception as exception:
        print(exception)


if __name__ == "__main__":
    import re
    from json import loads
    from supplier import config
    from supplier import initialize_driver
    from bs4 import BeautifulSoup
    from tinydb import TinyDB, Query
    from basic_files.base_json_template import JsonTemplate

    db = TinyDB(config.get("PRODUCT_INFO_DB_PATH"))
    url_db = TinyDB(config.get("PRODUCT_URL_DB_PATH"))
    urls = iter(url_db.all())
    query = Query()

    basic_data_matcher_condition = re.compile(r"var product_json = ")

    driver = initialize_driver()

    for index, url in enumerate(urls):
        try:
            scraper(product_url=url.get("url"), serial_number=index)
        except Exception as e:
            print(e)
