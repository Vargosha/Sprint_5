from tests.locators import HomePageLocators, AccountPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_account_page_opens_after_successful_login(browser,authorized_user):
    #Переход авторизированного пользователя в личный кабинет
    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/account'

def test_user_can_logout_via_logout_button_from_account_page(browser,authorized_user):
    #Выход из аккаунта через кнопку в личном кабинете
    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(AccountPageLocators.EXIT_BUTTON))
    browser.find_element(*AccountPageLocators.EXIT_BUTTON).click()

    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'
