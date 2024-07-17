#language: 
Feature: Criação de uma automação de preenchimento de um formulário

  Como usuário do site do Instituto Joga Junto
  Quero preencher o formulário de contato
  Para enviar o formulário preenchido
  
    Scenario: Preencher um formulário de envio de contato        
    Given nos estamos com a pagina do instituto aberta
    When nos preenchemos o formulário
    Then apertamos o botão de enviar