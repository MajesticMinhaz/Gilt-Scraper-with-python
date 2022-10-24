def get_products_url(page_url: str, tab_number: int):
    driver.switch_to.window(driver.window_handles[tab_number % 2])
    driver.get(f"{page_url}")
    time.sleep(3.5)
    single_page_products_list = WebDriverWait(driver=driver, timeout=10).until(method=single_page_products_list_finder)
    for product in single_page_products_list:
        data = {}
        try:
            data["url"] = product.find_element(
                by=By.TAG_NAME,
                value="a"
            ).get_attribute("href")

            if not db.contains(Query.url == str(data["url"])):
                db.insert(data)
                print(tab_number, data["url"])
            else:
                print(f"{tab_number}, Already Exists {data['url']}")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    import time
    from supplier import initialize_driver
    from supplier import config
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from tinydb import TinyDB, Query

    db = TinyDB(config.get("PRODUCT_URL_DB_PATH"))
    Query = Query()

    driver = initialize_driver()

    single_page_products_list_finder = ec.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div[class='product__caption']")
    )

    from_page = int(config.get("START_PAGE"))
    to_page = int(config.get("END_PAGE")) + 1

    for page_number in range(from_page, to_page):
        url = config.get("PAGE_URL").replace("{}", str(page_number)).strip()

        try:
            get_products_url(page_url=url, tab_number=page_number)
        except Exception as exception:
            print(exception)

    driver.close()
    print("Task complete.")
