# features/dictionary.feature

Feature: Pass a dictionary to Python

    Scenario: Pass a dictionary as a table
        Given the following dictionary
            | chave  | valor  |
            | chave1 | valor1 |
            | chave2 | valor2 |
        Then the dictionary should be correctly passed

