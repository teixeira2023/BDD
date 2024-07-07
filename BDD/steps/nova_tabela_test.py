from behave import given, when, then

@given('I am on the login page')
def step_impl(context):
    context.current_page = 'login'

@when('I enter the username "{username}" and the password "{password}"')
def step_impl(context, username, password):
    if username == 'user1' and password == 'pass1':
        context.login_message = 'Login successful'
    else:
        context.login_message = 'Invalid credentials'

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert context.login_message == message, f"Expected message to be {message} but got {context.login_message}"
