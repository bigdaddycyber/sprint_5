import pytest
from selenium import webdriver
import random
import string



@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def generate_email(self):
        letters = string.ascii_lowercase
        email = ''.join(random.choice(letters) for i in range(10)) + "@gmail.com"
        return email