from locators import HomePageLocators, ConstructorLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URLS

class TestUserConstructor:
    def test_user_redirected_to_constructor_when_clicking_constructor_button_in_account_page(self, browser, authorized_user):
        #Переход авторизированного пользователя в конструктор по клику на кнопку «Конструктор» из личного кабинета
        browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()
        browser.find_element(*HomePageLocators.CONSTRUCTOR_BUTTON).click()

        assert browser.current_url == URLS["main"]

    def test_user_redirected_to_constructor_when_clicking_logo_button_in_account_page(self, browser, authorized_user):
        #Переход авторизированного пользователя в конструктор по клику на логотип из личного кабинета
        browser.find_element(*HomePageLocators.ACCOUNT_PAGE_BUTTON).click()
        browser.find_element(*HomePageLocators.LOGO_BUTTON).click()

        assert browser.current_url == URLS["main"]

    def test_constructor_page_scrolled_to_bread_section_when_clicking_bread_button(self, browser, authorized_user):
        #Переход к разделу Булки при клике по кнопке «Булки»
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(HomePageLocators.BREAD_BUTTON))
        browser.find_element(*HomePageLocators.SAUCE_BUTTON).click()
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.BREAD_SECTION_UNSELECTED))
        browser.find_element(*HomePageLocators.BREAD_BUTTON).click()

        bread_section = WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.BREAD_SECTION_SELECTED))

        assert bread_section.is_displayed()

    def test_constructor_page_scrolled_to_sauce_section_when_clicking_sauce_button(self, browser, authorized_user):
        #Переход к разделу Соусы при клике по кнопке «Соусы»
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCE_SECTION_UNSELECTED))
        browser.find_element(*HomePageLocators.SAUCE_BUTTON).click()

        sauce_section = WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCE_SECTION_SELECTED))

        assert sauce_section.is_displayed()

    def test_constructor_page_scrolled_to_filling_section_when_clicking_filling_button(self, browser, authorized_user):
        #Переход к разделу Начинки при клике по кнопке «Начинки»
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.FILLING_SECTION_UNSELECTED))
        browser.find_element(*HomePageLocators.FILLING_BUTTON).click()

        filling_section = WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.FILLING_SECTION_SELECTED))

        assert filling_section.is_displayed()
