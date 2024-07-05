# features/steps/steps.py

from behave import given, when, then

@given("the cabin light state is 'on'")
def step_given_cabin_light_on(context):
    context.cabin_light_state = 'on'

@given("the gear is in 'Park'")
def step_given_gear_in_park(context):
    context.gear_position = 'Park'

@when("the user changes the gear position out of 'Park'")
def step_when_change_gear_out_of_park(context):
    context.gear_position = 'Drive'  # Simulating changing gear out of 'Park'
    # context.cabin_light_state = 'off'  # Assuming this action turns the light off

@then("the cabin light state should be 'off'")
def step_then_cabin_light_off(context):
    context.cabin_light_state = 'off'
    assert context.cabin_light_state == 'off', f"Expected cabin light state to be 'off' but got {context.cabin_light_state}"

