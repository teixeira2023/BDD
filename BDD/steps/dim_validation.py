from behave import *

@given('the new cabin light state is set to {new_initial_state}')
def step_given_cabin_light_state(context, new_initial_state):
    context.cabin_light_state = new_initial_state
    if context.cabin_light_state not in ['on', 'off']: raise ValueError(f"Error: new_initial_state is {new_initial_state}")

@given('the light brightness is {initial_light_brightness}')
def step_given_light_brightness(context, initial_light_brightness):
    context.initial_light_brightness = int(initial_light_brightness)
    if context.initial_light_brightness < 0 or context.initial_light_brightness > 100: raise ValueError(f"Error: initial_light_brightness is {initial_light_brightness}")

@when('the user holds the toggle button for more than one second {time_hold}')
def step_when_user_holds_the_toggle_button(context, time_hold):
    context.time_hold = int(time_hold)
    if context.time_hold < 1: raise ValueError(f"Error: time_hold is {time_hold}")

@then('the light brightness should decrease by 10 percent per second {light_brightness_new}')
def step_then_light_brightness_should_decrease(context, light_brightness_new):
    expected_brightness = context.initial_light_brightness - (context.initial_light_brightness * 0.10 * context.time_hold)
    assert int(light_brightness_new) == expected_brightness, \
        f"Error: expected brightness is {light_brightness_new}, but got {expected_brightness}"
    
    print(f"cabin_light_state: {context.cabin_light_state}")
    print(f"initial light brightness: {context.initial_light_brightness}")
    print(f"time hold: {context.time_hold}")
    print(f"light brightness new: {light_brightness_new}")

