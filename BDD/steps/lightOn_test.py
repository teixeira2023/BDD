# steps/cab_as_office_steps.py

from behave import given, when, then

@given('the cab light is {initial_state}')
def step_given_cab_light_state(context, initial_state):
    context.initial_light_state = initial_state
    assert initial_state in ['on', 'off'],f'Invalid initial state: {initial_state}'

@given('the timer is {initial_timer_state}' )
def step_given_timer_state(context, initial_timer_state):
    context.timer_state = initial_timer_state
    assert initial_timer_state in ['active', 'inactive'],f'Invalid initial state: {initial_timer_state}'

@given('the on timer is {initial_on_timer_value}')
def step_given_on_timer_value(context, initial_on_timer_value):
    context.on_timer_value = int(initial_on_timer_value)
    assert context.on_timer_value == context.on_timer_value, f'Invalid initial state: {initial_on_timer_value}'


@when('the driver shifts {range_selection}')
def step_when_driver_shifts(context, range_selection):
    context.range_selection = range_selection
    
    
    


@then('the cab light shall turns {cab_light_state}')
def step_then_cab_light_turns(context, cab_light_state):
    context.desired_cab_light_state = 'off' if context.initial_light_state == 'on' and context.range_selection == 'Not in Park' else 'on'
    assert context.desired_cab_light_state == cab_light_state, f"Erro: Esperado {cab_light_state}, mas obtido {context.desired_cab_light_state}"


@then('the timer goes {timer_state}')
def step_then_timer_goes(context, timer_state):
    context.timer_state_new = 'inactive' if context.initial_light_state == 'on' and context.range_selection == 'Not in Park' else 'active'
    assert context.timer_state_new == timer_state, f"Erro: Esperado {timer_state}, mas obtido {context.timer_state}"


@then('the on timer resets to {on_timer_value}')    
def step_then_on_timer_resets_to(context, on_timer_value):
    context.on_timer_value_desired = 0 if context.initial_light_state == 'on' and context.range_selection == 'Not in Park' else 10
    assert context.on_timer_value_desired == int(on_timer_value), f"Erro: Esperado {on_timer_value}, mas obtido {context.on_timer_value}"


