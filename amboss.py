import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils import get_google_driver, read_urls, write_urls

url = "https://amboss.space/"
driver = get_google_driver()


id_list = []


def main():
    id_list = read_urls()

    if len(id_list) == 0:
        id_list = get_first_page_anchor(driver)

    get_peers(id_list)

    write_urls(id_list)
    print(id_list)


def get_peers(urls):
    wait = WebDriverWait(driver, 30)
    tmp = []

    for url in urls:
        try:
            driver.get(url)

            if valida() == 0:
                continue

            try:
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//option[@value="50"]'))
                ).click()
            except Exception as e:
                print(e)
                continue

            select = Select(driver.find_element(By.XPATH, "//select"))
            if (select.first_selected_option.text) != "Show 50":
                select.select_by_value("50")

            time.sleep(5)

            anchors = driver.find_elements(by=By.TAG_NAME, value="a")

            if len(anchors) == 0:
                continue

            for anchor in anchors:
                address = anchor.get_attribute("href")

                if "https://amboss.space/node/" in address:
                    if address not in id_list:
                        tmp.append(address)
                        print(address)

        except Exception as e:
            print(e)
            continue

        write_urls(tmp)

    if len(tmp) > 0:
        id_list.append(tmp)
        get_peers(tmp)

    return tmp


def valida():
    time.sleep(1)

    errors = driver.find_elements(
        By.XPATH,
        '//*[text()="Error getting channels."] | //*[text()="Unable to find this node."]',
    )

    if len(errors) > 0:
        driver.refresh()
        time.sleep(1)

        errors = driver.find_elements(
            By.XPATH,
            '//*[text()="Error getting channels."] | //*[text()="Unable to find this node."]',
        )

    if len(errors) > 0:
        return 0
    else:
        return 1


def get_first_page_anchor(driver):
    wait = WebDriverWait(driver, 30)

    id_list = []

    driver.get(url)
    driver.refresh()
    time.sleep(5)

    try:
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//p[contains(text(), "Capacity")]')
            )
        )
    except Exception as e:
        print(e)
        raise e

    anchors = driver.find_elements(by=By.TAG_NAME, value="a")

    for anchor in anchors:
        address = anchor.get_attribute("href")

        if "https://amboss.space/node/" in address:
            if address not in id_list:
                id_list.append(address)
    return id_list


main()
