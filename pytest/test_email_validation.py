import re
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

# Carrega os cenários do arquivo de feature
scenarios('email_validation.feature')

# Função auxiliar para validar e-mails
def is_valid_email(email):
    # Regex simples para validação de e-mail
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Fixture para armazenar os dados do teste
@pytest.fixture
def email_data():
    return {}

# Passo Given para definir o e-mail com captura do parâmetro
@given(parsers.parse('I have an email "{email}"'))
def given_email(email, email_data):
    # Armazena o e-mail para uso nos próximos passos
    email_data['email'] = email

# Passo When para validar o e-mail
@when('I validate the email')
def validate_email(email_data):
    # Valida o e-mail e armazena o resultado
    email_data['is_valid'] = is_valid_email(email_data['email'])

# Passo Then para verificar se o e-mail é válido
@then('the email should be valid')
def email_should_be_valid(email_data):
    # Verifica se o e-mail é válido
    assert email_data['is_valid'] == True

# Passo Then para verificar se o e-mail é inválido
@then('the email should be invalid')
def email_should_be_invalid(email_data):
    # Verifica se o e-mail é inválido
    assert email_data['is_valid'] == False
