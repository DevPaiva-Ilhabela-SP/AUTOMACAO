from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = Firefox()

link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.NAME,"q")

input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(Keys.ENTER)


time.sleep(5)

result_seach = browser.find_elements(By.TAG_NAME,'h3')

check = False

for result in result_seach:
        if "Instituto Joga Junto" in result.text:
            result.click()
            print("Link selecionado")
        check = True
        break
title = browser.title
assert "Instituto Joga Junto" in title

browser.get("")
input_area.send_keys("Contato")
input_area.send_keys(Keys.ENTER)