from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('nos estamos com a pagina do instituto aberta')
def step_impl(context):
    
    title = context.browser.title
    assert 'Instituto Joga Junto' in title, "Página incorreta na busca"

@when('nos preenchemos o formulário')
def step_impl(context):
    input_nome = context.browser.find_element(By.ID, "nome")
    input_nome.send_keys('Rodrigo de Paiva Costa')

    input_email = context.browser.find_element(By.ID, "email")
    input_email.send_keys('rodrigo_paiva_costa@hotmail.com')

    input_assunto = context.browser.find_element(By.ID, "assunto")
    select = Select(input_assunto)
    select.select_by_index(5)

    input_msg = context.browser.find_element(By.ID, "mensagem")
    input_msg.send_keys('Meu primeiro script de automação - CYBERMASTERS')

@then('apertamos o botão de enviar')
def step_impl(context):
    #import ipdb;ipdb.sset_trace()
    button_enviar = context.browser.find_element(By.XPATH, "//button[@type='submit']")
    button_enviar.submit()

    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    assert 'Dados recebidos' in alert.text, "Dados não recebidos"