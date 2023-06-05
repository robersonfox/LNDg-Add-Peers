def get_google_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()

    # comente a linha abaixo para ver o navegador
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome("chromedriver", options=chrome_options)

    # def interceptor(request):
    #     del request.headers["Referer"]  # Delete the header first

    #     header = {
    #         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    #         "X-Requested-With": "XMLHttpRequest",
    #     }

    #     request.headers["Referer"] = header

    # driver.request_interceptor = interceptor

    return driver


def write_urls(list=list, file="./list.txt"):
    try:
        f = open(file, "a")

        for url in list:
            f.writelines(url)

        f.close()
    except Exception as e:
        print(e)
        return False


def read_urls(file="./list.txt"):
    try:
        f = open(file, "r")
        c = f.readlines()

        if len(c) > 0:
            return c

        return []
    except Exception as e:
        print(e)
        return []
