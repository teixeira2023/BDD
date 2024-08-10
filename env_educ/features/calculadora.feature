Feature: Operações básicas de uma calculadora

    Scenario: Somar dois números
        Given que o usuário tem uma calculadora
        When o usuário soma 5 e 7
        Then o resultado deve ser 12

    Scenario: Subtrair dois números
        Given que o usuário tem uma calculadora
        When o usuário subtrai 9 e 7
        Then o resultado deve ser 2
