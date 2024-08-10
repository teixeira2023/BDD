from behave import given, when, then
import time
from utils.calculadora import Calculadora


# Instância global da calculadora
calculadora = Calculadora()

@given('que o usuário tem uma calculadora')
def step_given_usuario_tem_calculadora(context):
    # Inicialmente, a calculadora já está criada e pronta para uso
    time.sleep(1)
    pass

@when('o usuário soma {a:d} e {b:d}')
def step_when_usuario_soma(context, a, b):
    calculadora.somar(a, b)
    time.sleep(1)

@then('o resultado deve ser {resultado:d}')
def step_then_resultado_deve_ser(context, resultado):
    time.sleep(1)
    assert calculadora.obter_resultado() == resultado, \
        f'Esperado {resultado}, mas obteve {calculadora.obter_resultado()}'
        

@given('que o usuário tem uma calculadora com {x:d} e {y:d}')
def step_given_calculadora_com(context, x, y):
    pass
    time.sleep(1)
    
@when('o usuário subtrai {x:d} e {y:d}')
def step_when_calculadora_subtrai(context, x, y):
    calculadora.subtrair(x, y)
    time.sleep(1)
    
@then('o resultado deve ser {resultado:d}')
def step_then_resultado_deve_ser(context, resultado):
    time.sleep(1)
    assert calculadora.obter_resultado() == resultado   