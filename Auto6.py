
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def iniciar_browser():
    return Firefox()

def abrir_pagina(browser, link):
    browser.get(link)

def buscar_e_clicar_resultado(browser, termo_busca, resultado_desejado):
    try:
        input_area = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        input_area.send_keys(termo_busca)
        input_area.send_keys(Keys.ENTER)
        
        result_search = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'h3')))
        
        for result in result_search:
            if resultado_desejado in result.text:
                result.click()
                print("Link encontrado e clicado!")
                return True
        return False
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Erro ao buscar e clicar no resultado: {e}")
        return False

def preencher_formulario(browser, dados_formulario):
    try:
        input_nome = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "nome")))
        input_nome.send_keys(dados_formulario['nome'])
        
        input_email = browser.find_element(By.ID, "email")
        input_email.send_keys(dados_formulario['email'])
        
        input_assunto = browser.find_element(By.ID, "assunto")
        select = Select(input_assunto)
        select.select_by_index(dados_formulario['assunto'])
        
        input_msg = browser.find_element(By.ID, "mensagem")
        input_msg.send_keys(dados_formulario['mensagem'])
        
        button_enviar = browser.find_element(By.XPATH, "//button[@type='submit']")
        button_enviar.click()
        
        print("Formulário enviado com sucesso!")
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Erro ao preencher e enviar o formulário: {e}")

def main():
    browser = iniciar_browser()
    link = 'https://google.com'
    
    try:
        abrir_pagina(browser, link)
        
        if buscar_e_clicar_resultado(browser, 'Instituto Joga Junto', 'Instituto Joga Junto'):
            WebDriverWait(browser, 10).until(EC.title_contains('Instituto Joga Junto'))
            
            dados_formulario = {
                'nome': 'Rodrigo de Paiva Costa',
                'email': 'rodrigo_paiva_costa@hotmail.com',
                'assunto': 5,
                'mensagem': 'Meu primeiro script de automação - CYBERMASTERS'
            }
            
            preencher_formulario(browser, dados_formulario)
        else:
            print("Resultado desejado não encontrado.")
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()