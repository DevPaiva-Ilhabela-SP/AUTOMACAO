from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = Firefox()

browser.get("https://google.com")

input_area = browser.find_element(By.NAME,"q")

input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(Keys.ENTER)

time.sleep(10)

result_search = browser.find_elements(By.TAG_NAME,'h3')
check = False

for result in result_search:
        if "Instituto Joga Junto" in result.text:
            result.click()
            print("Link selecionado")
        check = True
        break
title = browser.title
assert "Instituto Joga Junto" in title

browser.find_element(By.XPATH, '//*[@id="mensagem"]')
browser.send_keys("Meu primeiro script de automação - CYBERMASTERS")
    # Encontrar o campo de entrada (ajuste o seletor conforme necessário)
result_search = browser.find_elements(By.TAG_NAME, 'a')
check = False
for result in result_search:
        if "Contato" in result.text:
            result.click()
            print("Contato selecionado")
        check = True
        break

    # Enviar a mensagem
#input_area.send_keys('Meu primeiro script de automação - CYBERMASTERS')
#input_area.send_keys(Keys.RETURN)  # Enviar a mensagem (se necessário)

    # Esperar um pouco para ver a ação
time.sleep(10)

# Fechar o navegador
browser.quit()