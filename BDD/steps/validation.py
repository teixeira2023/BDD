from behave import given, when, then

# Inicializando os estados
@given('the current cabin light state is {initial_state}')
def step_given_cabin_light_state(context, initial_state):
    context.cabin_light_state = initial_state

@given('the range selection is {range_value}')
def step_given_range_selection(context,range_value):
    context.range_selection = range_value

@given('the vehicle power mode is greater than 10')
def step_given_vehicle_power_mode(context):
    context.vehicle_power_mode = 20  # Valor aleatório superior a 10

@when('the user presses the toggle button {toggle_value}')
def step_when_user_presses_toggle_button(context, toggle_value):
    
    
    context.toggle_value = toggle_value
    should_light_be_on = (
        context.cabin_light_state == 'off' or context.cabin_light_state == 'on' and
        context.range_selection == 'Park' and
        context.vehicle_power_mode > 10 and
        context.toggle_value == 'pressed'
    )
    context.cabin_curr_light_state = 'on' if should_light_be_on else 'off'
    
    
@then('the light state should be {final_state}')
def step_then_light_state_should_be(context,final_state):
    assert context.cabin_curr_light_state == final_state, f"Erro: Esperado {final_state}, mas obtido {context.cabin_curr_light_state}"
    print(f"cabin_light_state: {context.cabin_light_state}")
    print(f"range_selection: {context.range_selection}")
    print(f"vehicle_power_mode: {context.vehicle_power_mode}")
    # print(f"toggle_value: {toggle_value}")
    print(f"cabin_curr_light_state: {context.cabin_curr_light_state}")