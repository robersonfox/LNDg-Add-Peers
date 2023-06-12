import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import get_google_driver, read_urls, write_urls

# LNDg Credentials
lndg_user = "lndg-admin"
lndg_pass = "PASSWORD"
lndg_url = "http://192.168.0.63:8889/"

# Umbrel Credentials
umbrel_pass = "PASSWORD"
umbrel_login_url = "http://192.168.0.63:8889/"

driver = get_google_driver()


def main():
    import os

    driver.get(umbrel_login_url)
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))

    pass_input = driver.find_element(By.XPATH, '//input[@type="password"]')
    pass_input.send_keys(umbrel_pass)
    pass_input.submit()
    time.sleep(1)

    driver.get(lndg_url)

    user_name = driver.find_element(By.XPATH, '//input[@name="username"]')
    user_name.send_keys(lndg_user)

    user_pass = driver.find_element(By.XPATH, '//input[@name="password"]')
    user_pass.send_keys(lndg_pass)
    user_pass.submit()

    time.sleep(1)

    success_list = read_urls("./success.txt")

    print(f"Success list: {len(success_list)}")

    with open("./list.txt") as infile:
        for url in infile:
            u = url.rsplit("/")[-1].replace("\n", "")

            if url in success_list:
                continue

            clear = lambda: os.system("clear")
            clear()

            print(f"Trying {u}...")
            print(f"Success list: {len(success_list)}")

            driver.get(umbrel_login_url)
            peer_input = driver.find_element(By.XPATH, '//input[@id="peer_id"]')

            try:
                peer_input.send_keys(f"{u}")
                peer_input.send_keys(Keys.RETURN)

                wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//div[@id="messages"]'))
                )

                success = driver.find_element(By.XPATH, '//div[@id="messages"]')
                text = success.text

                print(f"Peer {u} {text}!")

                if "success" in text or "connected" in text:
                    write_urls(url, "./success.txt")

                time.sleep(1)
            except Exception as e:
                print(e)
                continue


main()
