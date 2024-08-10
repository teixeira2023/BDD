# Este é um arquivo de feature usando a sintaxe Gherkin.
# Ele descreve o comportamento esperado de validação de e-mail.

Feature: Email validation
  # Esta feature descreve a validação de endereços de e-mail.
  
  Scenario: Valid email
    # Este cenário descreve a validação de um e-mail válido.
    Given I have an email "user@example.com"
    When I validate the email
    Then the email should be valid

  Scenario: Invalid email
    # Este cenário descreve a validação de um e-mail inválido.
    Given I have an email "user@example"
    When I validate the email
    Then the email should be invalid
