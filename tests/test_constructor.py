from tests.locators import HomePageLocators, ConstructorLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_user_redirected_to_constructor_when_clicking_constructor_button_in_account_page(browser, authorized_user):
    #Переход авторизированного пользователя в конструктор по клику на кнопку «Конструктор» из личного кабинета
    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()
    browser.find_element(*HomePageLocators.CONSTRUCTOR_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_user_redirected_to_constructor_when_clicking_logo_button_in_account_page(browser, authorized_user):
    #Переход авторизированного пользователя в конструктор по клику на логотип из личного кабинета
    browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()
    browser.find_element(*HomePageLocators.LOGO_BUTTON).click()

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_constructor_page_scrolled_to_bread_section_when_clicking_bread_button(browser, authorized_user):
    #Переход к разделу Булки при клике по кнопке «Булки»
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.BREAD_BUTTON))
    element = browser.find_element(*ConstructorLocators.BREAD_SECTION)
    browser.find_element(*HomePageLocators.FILLING_BUTTON).click()
    time.sleep(1)
    browser.find_element(*HomePageLocators.BREAD_BUTTON).click()
    time.sleep(1)

    is_in_viewport = browser.execute_script("""
    const rect = arguments[0].getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
""", element)

    assert is_in_viewport is True

def test_constructor_page_scrolled_to_sauce_section_when_clicking_sauce_button(browser, authorized_user):
    #Переход к разделу Соусы при клике по кнопке «Соусы»
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.SAUCE_BUTTON))
    element = browser.find_element(*ConstructorLocators.SAUCE_SECTION)
    browser.find_element(*HomePageLocators.FILLING_BUTTON).click()
    time.sleep(1)
    browser.find_element(*HomePageLocators.SAUCE_BUTTON).click()
    time.sleep(1)

    is_in_viewport = browser.execute_script("""
    const rect = arguments[0].getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
""", element)

    assert is_in_viewport is True

def test_constructor_page_scrolled_to_filling_section_when_clicking_filling_button(browser, authorized_user):
    #Переход к разделу Начинки при клике по кнопке «Начинки»
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.FILLING_BUTTON))
    element = browser.find_element(*ConstructorLocators.FILLING_SECTION)
    browser.find_element(*HomePageLocators.FILLING_BUTTON).click()
    time.sleep(1)

    is_in_viewport = browser.execute_script("""
    const rect = arguments[0].getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
""", element)

    assert is_in_viewport is True
