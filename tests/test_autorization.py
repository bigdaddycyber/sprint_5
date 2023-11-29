import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators

class TestAutorization:
    
    def test_enter_button_on_main_page(self):
        driver = webdriver.Chrome()
        current_url = "https://stellarburgers.nomoreparties.site/"
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        assert current_url
        
          
    def test_enter_button_through_lk(self):
        driver = webdriver.Chrome()
        current_url = "https://stellarburgers.nomoreparties.site/"
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        return current_url
        
    def test_enter_button_through_formregistration(self):
        driver = webdriver.Chrome()
        current_url = "https://stellarburgers.nomoreparties.site/register"
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        driver.find_element(*MainLocators.BUTTON_REGISTRAION).click()
        driver.find_element(*RegPage.BUTTON_ENTER_FORMREG).click()
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        return current_url
        
    def test_enter_button_through_from_recoveryform(self):
        driver = webdriver.Chrome()
        current_url = "https://stellarburgers.nomoreparties.site/register"
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*MainLocators.BUTTON_LOGIN_LK).click() 
        driver.find_element(*RegPage.BUTTON_ENTER_RECOVERYFORM).click()
        driver.find_element(*RegPage.BUTTON_ENTER_FOGOTPASS).click()
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        return current_url
