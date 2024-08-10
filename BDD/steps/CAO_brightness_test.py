from behave import given, when, then

@given('the current cabin light is "{stateCabinLight}"')
def step_impl(context, stateCabinLight):
    context.stateCabinLight = stateCabinLight

@when('the cab as office hard button is "pressed"')
def step_impl(context):
    context.button_pressed = True

@when('the value of dimming is "{valueDimming}"')
def step_impl(context, value):
    context.valueDimming = int(valueDimming)

@when('the light control menu is "displayed"')
def step_impl(context):
    context.menu_displayed = True

@when('the hold timer is "{time}" seconds')
def step_impl(context, time):
    context.hold_timer = float(time)

@when('the driver releases the cabin as office hard button')
def step_impl(context):
    context.button_pressed = False

@then('the cab as Office Light feature should set the luminosity to "{new_value}" %')
def step_impl(context, new_value):
    new_value = int(new_value)
    assert context.valueDimming_new == new_value, f"Expected luminosity of {new_value}%, got {context.valueDimming_new}%"
