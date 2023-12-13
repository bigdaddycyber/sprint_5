from selenium import webdriver
from selenium.webdriver.common.by import By



class RegPage:
    
    BUTTON_ENTER_IN_ACC = (By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")
    NAME_FORM = (By.XPATH, "(.//input[@name = 'name'])")
    EMAIL_FORM = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FORM = (By.XPATH, "//input[@name = 'Пароль']")
    BUTTON_REG_ACC = (By. XPATH, "//button[text() = 'Зарегистрироваться']")
    BUTTON_NAME = (By.XPATH, "(.//input[@name = 'name'])")
    BUTTON_EMAIL = (By.XPATH, "//input[@name = 'Пароль']")
    BUTTON_ENTER_FORM_REG = (By.LINK_TEXT, '/register')
    BUTTON_ENTER_RECOVERYFORM = (By.CLASS_NAME, "Auth_link__1fOlj")
    BUTTON_ENTER_FOGOTPASS = (By.LINK_TEXT, '/login')
    

class MainLocators:
    
    BUTTON_LOGIN_LK = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    BUTTON_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    BUTTON_REGISTRAION = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")
    BUTTON_CONSTRUKTOR = (By.XPATH, ".//p[text() = 'Конструктор']")
    LOGO = (By.LINK_TEXT, "/")
    BULKA = (By.XPATH, ".//span[text() = 'Булки']")
    SOUCE = (By.XPATH, ".//span[text() = 'Соусы']")
    NACHINKA = (By.XPATH, ".//span[text() = 'Начинки']")
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
