import pytest

from pages.login_page import LoginPage
from utilities import test_data
import re
@pytest.fixture
def login_setup(page):
    login_page = LoginPage(page)
    login_page.navigate_to()
    yield login_page

def test_valid_login(login_setup):
    login_setup.login(test_data.credentials["valid_username"], test_data.credentials["valid_password"])

def test_invalid_login(login_setup):
    login_setup.login(test_data.credentials["invalid_username"], test_data.credentials["invalid_password"])

    current_error_message = re.sub(r"\s+", " ", login_setup.get_error_message())

    assert current_error_message == "Invalid Login details or Your Password might have expired. Click here to reset your password"