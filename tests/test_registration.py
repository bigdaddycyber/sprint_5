import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators


class TestRegisrtrationPage:
    
    def test_successful_registration(self,browser):
        browser.get("https://stellarburgers.nomoreparties.site")
        browser.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        browser.find_element(*RegPage.BUTTON_ENTER_FORM_REG).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "/register")
        browser.find_element(*RegPage.NAME_FORM).send_keys("Test123456789")
        browser.find_element(*RegPage.EMAIL_FORM).send_keys(self.generate_email())
        browser.find_element(*RegPage.PASSWORD_FORM).send_keys("test12345")
        browser.find_element(*RegPage.BUTTON_REG_ACC).click()
        assert browser.current  == 'https://stellarburgers.nomoreparties.site/'

    
    def test_error_for_nocorrect_password(self,browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "/login")
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        assert browser.find_element(By. CLASS_NAME, 'input__error text_type_main-default')
        


