# features/steps/dictionary_steps.py

import json
from behave import given, then

@given('the following dictionary as JSON')
def step_given_dictionary_json(context):
    context.dictionary = json.loads(context.text)

@then('the dictionary should be correctly passed in json format')
def step_then_check_dictionary(context):
    expected_dictionary = {
        'light_state': 'on',
        'feature_state': 'enabled'
    }
    assert context.dictionary == expected_dictionary, f"Expected {expected_dictionary} but got {context.dictionary}"
