from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import (HomePageLocators, LoginPageLocators,
                      RegistrationPageLocators, ForgotPageLocators)


def test_user_can_login_via_login_button_on_home_page(browser):
    #Вход в аккаунт по кнопке «Войти в аккаунт» на главной
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.LOGIN_PAGE_BUTTON))
    browser.find_element(*HomePageLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('numbertwo@yandex.ru')
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('Hsrshfsh')
    browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account'

def test_user_can_login_via_profile_button(browser):
    #Вход в аккаунт через кнопку «Личный кабинет»
    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('numbertwo@yandex.ru')
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('Hsrshfsh')
    browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account'

def test_user_can_login_via_login_button_on_registration_page(browser):
    #Вход в аккаунт через кнопку «Войти» в форме регистрации
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.LOGIN_PAGE_BUTTON))
    browser.find_element(*HomePageLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTRATION_PAGE_BUTTON))
    browser.find_element(*LoginPageLocators.REGISTRATION_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(RegistrationPageLocators.LOGIN_PAGE_BUTTON))
    browser.find_element(*RegistrationPageLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('numbertwo@yandex.ru')
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('Hsrshfsh')
    browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account'

def test_user_can_login_via_login_button_on_forgot_password_page(browser):
    #Вход в аккаунт через кнопку «Войти» в форме восстановления пароля
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.LOGIN_PAGE_BUTTON))
    browser.find_element(*HomePageLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.FORGOT_PASSWORD_PAGE_BUTTON))
    browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(ForgotPageLocators.LOGIN_PAGE_BUTTON))
    browser.find_element(*ForgotPageLocators.LOGIN_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys('numbertwo@yandex.ru')
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('Hsrshfsh')
    browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account'
