from behave import given, when, then

@given('I reset the table')
def step_impl(context):
    context.table_data = []

@given('I have a table with the following rows')
def step_impl(context):
    context.table_data = []
    for row in context.table:
        context.table_data.append({'chave': row['chave'], 'valor': row['valor']})

@when('I send the table to the step file')
def step_impl(context):
    # Simulate sending the table to the step file, e.g., store it somewhere
    context.stored_table = context.table_data

@then('I should see the table in the step file')
def step_impl(context):
    assert context.stored_table == context.table_data, "The table was not stored correctly"
