from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


servico = Service (GeckoDriverManager().install())

navegador = webdriver.Firefox(service = servico)

navegador.get("https://www.google.com/")
navegador.find_element(By.NAME,"q")
navegador.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys("Instituto Joga Junto")
navegador.find_elements(By.TAG_NAME,'h3').send_keys(Keys.ENTER)
