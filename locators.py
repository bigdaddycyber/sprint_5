from selenium import webdriver
from selenium.webdriver.common.by import By


class RegPage:
    
    BUTTON_ENTER_IN_ACC = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")
    NAME_FORM = (By.XPATH, "(.//input[@name = 'name'])[1]")
    EMAIL_FORM = (By.XPATH, "(.//input[@name = 'name'])[2]")
    PASSWORD_FORM = (By.XPATH, "//input[@name = 'Пароль']")
    BUTTON_REG_ACC = (By. XPATH, "//button[text() = 'Зарегистрироваться']")
    BUTTON_NAME = (By.XPATH, "(.//input[@name = 'name'])")
    BUTTON_EMAIL = (By.XPATH, "//input[@name = 'Пароль']")
    BUTTON_ENTER_FORMREG = (By.XPATH, ".//a[text() = 'Войти']")
    BUTTON_ENTER_RECOVERYFORM = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    BUTTON_ENTER_FOGOTPASS = (By.XPATH, ".//a[text() = 'Войти']")
    

class MainLocators:
    
    BUTTON_LOGIN_LK = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    BUTTON_LOG_IN_ACC = (By.XPATH, "button[text() = 'Войти в аккаунт']")
    BUTTON_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    BUTTON_REGISTRAION = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")
    BUTTON_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")
    BUTTON_CONSTRUKTOR = (By.XPATH, ".//p[text() = 'Конструктор']")
    LOGO = (By.LINK_TEXT, "/")
    BULKA = (By.XPATH, ".//span[text() = 'Булки']")
    SOUCE = (By.XPATH, ".//span[text() = 'Соусы']")
    NACHINKA = (By.XPATH, ".//span[text() = 'Начинки']")
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
