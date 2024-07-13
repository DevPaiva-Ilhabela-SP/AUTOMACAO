from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
browser = Firefox()

link = "https://google.com"

browser.get(link)

input_area = browser.find_element(By.NAME,"q")

input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(keys.Enter)
from time import sleep; sleep(3)
link_ijj = browser.find_element(By.TAG_NAME,'h3')
print("result_search")


check = False

while check == False:


    for result in result_search:
        if result.text == "Instituto Joga Junto":
            result.click()
            print("AEEEEEEEEEE")
        check = True