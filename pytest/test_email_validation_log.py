import re
import logging
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    email_data['email'] = email
    logger.info(f"Given: I have an email '{email}'")

# Passo When para validar o e-mail
@when('I validate the email')
def validate_email(email_data):
    email_data['is_valid'] = is_valid_email(email_data['email'])
    logger.info(f"When: I validate the email '{email_data['email']}'")

# Passo Then para verificar se o e-mail é válido
@then('the email should be valid')
def email_should_be_valid(email_data):
    assert email_data['is_valid'] == True
    logger.info(f"Then: The email '{email_data['email']}' should be valid - Test Passed")

# Passo Then para verificar se o e-mail é inválido
@then('the email should be invalid')
def email_should_be_invalid(email_data):
    assert email_data['is_valid'] == False
    logger.info(f"Then: The email '{email_data['email']}' should be invalid - Test Passed")
