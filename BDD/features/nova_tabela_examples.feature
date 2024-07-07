Feature: Teste com múltiplos exemplos
  Testando múltiplos conjuntos de dados com Scenario Outline

  @feat2 @scenario2
  Scenario Outline: Teste de login com múltiplos usuários
    Given I am on the login page
    When I enter the username "<username>" and the password "<password>"
    Then I should see the message "<message>"

  Examples:
    | username  | password | message            |
    | user1     | pass1    | Login successful   |
    | user2     | wrongpass| Invalid credentials|
