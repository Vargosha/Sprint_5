from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import HomePageLocators, LoginPageLocators, RegistrationPageLocators
from config import URLS

class TestUserRegistration:
    def test_registration_creates_new_user(self,browser,random_user):
        #Регистрация нового пользователя
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.LOGIN_PAGE_BUTTON))
        browser.find_element(*HomePageLocators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTRATION_PAGE_BUTTON))
        browser.find_element(*LoginPageLocators.REGISTRATION_PAGE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.SUBMIT_BUTTON))
        browser.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(random_user['name'])
        browser.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(random_user['email'])
        browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(random_user['password'])
        browser.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        #Вход в созданный аккаунт
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.SUBMIT_BUTTON))
        browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(random_user['email'])
        browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(random_user['password'])
        browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

        assert browser.current_url == URLS["account"]

    def test_registration_with_password_less_than_6_characters_shows_error(self,browser,random_user):
        #Регистрация нового пользователя с паролем менее 6 символов
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.LOGIN_PAGE_BUTTON))
        browser.find_element(*HomePageLocators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTRATION_PAGE_BUTTON))
        browser.find_element(*LoginPageLocators.REGISTRATION_PAGE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.SUBMIT_BUTTON))
        browser.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(random_user['name'])
        browser.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(random_user['email'])
        browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('asdfg')
        browser.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        error_text = browser.find_element(*RegistrationPageLocators.PASSWORD_ERROR).text

        assert error_text == 'Некорректный пароль'

    def test_registration_with_empty_password_does_not_creates_new_user(self,browser,random_user):
        #Регистрация нового пользователя с пустым паролем
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.LOGIN_PAGE_BUTTON))
        browser.find_element(*HomePageLocators.LOGIN_PAGE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.REGISTRATION_PAGE_BUTTON))
        browser.find_element(*LoginPageLocators.REGISTRATION_PAGE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.SUBMIT_BUTTON))
        browser.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(random_user['name'])
        browser.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(random_user['email'])
        browser.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys('')
        browser.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

        assert browser.current_url == URLS["register"]
