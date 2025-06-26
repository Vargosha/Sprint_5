class HomePageLocators:
    ACCOUNT_PAGE_BUTTON = ("xpath", ".//p[text()= 'Личный Кабинет']") #Кнопка Личный Кабинет
    LOGIN_PAGE_BUTTON = ("xpath", ".//button[text() = 'Войти в аккаунт']") #Кнопка Войти в аккаунт
    CONSTRUCTOR_BUTTON = ("xpath", ".//p[text() = 'Конструктор']") #Кнопка Конструктор
    LOGO_BUTTON = ("xpath", ".//div[@class='AppHeader_header__logo__2D0X2']//a[@href='/']") #Кнопка с логотипом
    BREAD_BUTTON = ("xpath", ".//span[text() ='Булки']") #Кнопка Булки
    SAUCE_BUTTON = ("xpath", ".//span[text() ='Соусы']") #Кнопка Соусы
    FILLING_BUTTON = ("xpath", ".//span[text() ='Начинки']") #Кнопка Начинки

class LoginPageLocators:
    EMAIL_INPUT = ("xpath", ".//input[@name='name']") #Поле ввода Email
    PASSWORD_INPUT = ("xpath", ".//input[@name='Пароль']") #Поле ввода Пароль
    SUBMIT_BUTTON = ("xpath", ".//button[text() = 'Войти']") #Кнопка Войти
    REGISTRATION_PAGE_BUTTON = ("xpath", ".//a[text() = 'Зарегистрироваться']") #Кнопка Зарегистрироваться
    FORGOT_PASSWORD_PAGE_BUTTON = ("xpath", ".//a[text() = 'Восстановить пароль']") #Кнопка Восстановить пароль

class RegistrationPageLocators:
    NAME_INPUT = ("xpath", ".//fieldset[1]//input[@name='name']") #Поле ввода Имя
    EMAIL_INPUT = ("xpath", ".//fieldset[2]//input[@name='name']") #Поле ввода Email
    PASSWORD_INPUT = ("xpath", ".//input[@name='Пароль']") #Поле ввода Пароль
    SUBMIT_BUTTON = ("xpath", ".//button[text() = 'Зарегистрироваться']") #Кнопка Зарегистрироваться
    LOGIN_PAGE_BUTTON = ("xpath", ".//a[text() = 'Войти']") #Кнопка Войти
    PASSWORD_ERROR = ("xpath", ".//p[text() = 'Некорректный пароль']") #Ошибка Некорректный пароль

class AccountPageLocators:
    EXIT_BUTTON = ("xpath", ".//button[text() = 'Выход']") #Кнопка Выход

class ForgotPageLocators:
    LOGIN_PAGE_BUTTON = ("xpath", ".//a[text() = 'Войти']")  #Кнопка Войти

class ConstructorLocators:
    BREAD_SECTION_SELECTED = ("xpath",
                              ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Булки']") #Активная секция Булки
    BREAD_SECTION_UNSELECTED = ("xpath",
                                ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Булки']") #Неактивная секция Булки
    SAUCE_SECTION_SELECTED = ("xpath",
                              ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Соусы']") #Активная секция Соусы
    SAUCE_SECTION_UNSELECTED = ("xpath",
                                ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Соусы']") #Неактивная секция Соусы
    FILLING_SECTION_SELECTED = ("xpath",
                              ".//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Начинки']") #Активная секция Начинки
    FILLING_SECTION_UNSELECTED = ("xpath",
                                ".//div[@class = 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']//span[text() = 'Начинки']") #Неактивная секция Начинки
