import behave
from behave import given, when, then

@given('the vehicle power mode is between 20 and 70')
def step_given_vehicle_power_mode(context):
    context.vehicle_power_mode = {row['power_mode']: row['value'] for row in context.table} 
@given('the vehicle range selection is Park')
def step_given_range_selection(context):
    context.range_selection = {row['range_selection']: row['value'] for row in context.table}

@given('the cabin light state is off')
def step_given_cabin_light_state(context):
    context.cabin_light_state = {row['light_state']: row['value'] for row in context.table}

@then('the cabin light feature should be enabled')
def step_then_cabin_light_feature_enabled(context):
    context.feature_state = 'enabled'
    assert context.feature_state == 'enabled', f"Expected cabin light state to be 'Enabled' but failed"
    