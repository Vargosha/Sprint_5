import pytest
from helpers import generate_email, generate_password
from selenium import webdriver
from locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URLS


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(URLS["main"])
    yield driver
    driver.quit()

@pytest.fixture
def random_user():
    return {
        'email': generate_email(),
        'password': generate_password(),
        'name': 'Test User'
    }

@pytest.fixture
def authorized_user(browser):
    browser.get(URLS["login"])
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('numbertwo@yandex.ru')
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('Hsrshfsh')
    browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
