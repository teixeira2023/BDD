Feature: Criação de uma tabela de teste
  Criação de uma tabela para testar o envio de informações ao arquivo step do framework behave

  Background:
    Given I reset the table

  @feat1 @scenario1
  Scenario: Criação de uma tabela
    Given I have a table with the following rows
      | chave | valor  |
      | info1 | value1 |
      | info2 | value2 |
    When I send the table to the step file
    Then I should see the table in the step file
