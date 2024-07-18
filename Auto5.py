from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = Firefox()

link = 'https://google.com'
browser.get(link)

input_area = browser.find_element(By.NAME, "q")
input_area.send_keys('Instituto Joga Junto')
input_area.send_keys(Keys.ENTER)

time.sleep(10) 

result_search = browser.find_elements(By.TAG_NAME, 'h3')

check = False

for result in result_search:
    if 'Instituto Joga Junto' in result.text:
        result.click()
        print("Link encontrado e clicado!")
        check = True
        break

title = browser.title
assert 'Instituto Joga Junto' in title, "Página incorreta na busca"

input_nome = browser.find_element(By.ID, "nome")
input_nome.send_keys('Rodrigo de Paiva Costa')

input_email = browser.find_element(By.ID, "email")
input_email.send_keys('rodrigo_paiva_costa@hotmail.com')

input_assunto = browser.find_element(By.ID, "assunto")
select = Select(input_assunto)
select.select_by_index(5)

input_msg = browser.find_element(By.ID, "mensagem")
input_msg.send_keys('Meu primeiro script de automação - CYBERMASTERS')

button_enviar = browser.find_element(By.XPATH, "//button[@type='submit']")
button_enviar.submit()

time.sleep(10)

browser.quit()