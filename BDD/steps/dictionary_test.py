# features/steps/dictionary_steps.py

from behave import given, then

@given('the following dictionary')
def step_given_dictionary(context):
    context.dictionary = {row['chave']: row['valor'] for row in context.table}

@then('the dictionary should be correctly passed')
def step_then_check_dictionary(context):
    expected_dictionary = {
        'chave1': 'valor1',
        'chave2': 'valor2'
    }
    assert context.dictionary == expected_dictionary, f"Expected {expected_dictionary} but got {context.dictionary}"
