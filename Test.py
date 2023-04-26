import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.maximize_window()
# driver.get("https://mail.yandex.com/")
driver.get("https://mail360.yandex.com/premium-plans?from=mail_landing")
driver.implicitly_wait(10)
try:
    button = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[3]/section[1]/div/a[2]')
    print(f'button:{button}')
    button.click()
except NoSuchElementException as e:
    print("没找到按钮")
    driver.quit();

time.sleep(5)
