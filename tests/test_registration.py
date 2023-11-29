import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage




class TestRegisrtrationPage:
    
    def test_successful_registration(self):
        driver = webdriver.Chrome()
        current_url = "https://stellarburgers.nomoreparties.site/register"
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegPage.NAME_FORM).send_keys("Test123456789")
        driver.find_element(*RegPage.EMAIL_FORM).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.PASSWORD_FORM).send_keys("test12345")
        driver.find_element(*RegPage.BUTTON_REG_ACC).click()
        return current_url
    
    def test_error_for_nocorrect_password(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
