from json import loads
from undetected_chromedriver import Chrome
from undetected_chromedriver import ChromeOptions
from dotenv import dotenv_values

config = dotenv_values(dotenv_path="./.env")

with open(file=config.get("COOKIE_PATH"), mode="r") as read_cookie_file:
    cookie = loads(read_cookie_file.read())


def initialize_driver() -> Chrome:
    options = ChromeOptions()
    driver = Chrome(
        driver_executable_path=config.get("DRIVER_PATH"),
        options=options
    )

    driver.get(config.get("BASE_URL"))

    for cookie_data in cookie:
        customized_cookie = dict()
        customized_cookie['domain'] = cookie_data.get("domain")
        customized_cookie['name'] = cookie_data.get("name")
        customized_cookie['value'] = cookie_data.get("value")

        driver.add_cookie(cookie_dict=customized_cookie)

    driver.refresh()
    driver.switch_to.new_window(type_hint='tab')
    return driver
