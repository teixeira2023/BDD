import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Carregar os cenários da feature
scenarios('../features/turn_on_light.feature')

# Variáveis globais para manter o estado
light_state = ""
power_mode = 0

@given(parsers.parse('the cabin light state is {initial_state}'))
def given_cabin_light_state(initial_state):
    global light_state
    light_state = initial_state

@given('the range selection is Park')
def given_range_selection():
    pass  # Nenhuma ação necessária para este passo

@given('the vehicle power mode is greater than 10')
def given_vehicle_power_mode():
    global power_mode
    power_mode = 20  # Definir um valor válido maior que 10

@when('the user presses the toggle button')
def when_user_presses_toggle_button():
    global light_state
    if light_state == 'off':
        light_state = 'on'
    else:
        light_state = 'off'

@then(parsers.parse('the light state should be {final_state}'))
def then_light_state_should_be(final_state):
    assert light_state == final_state, f"Erro: Esperado {final_state}, mas obtido {light_state}"
