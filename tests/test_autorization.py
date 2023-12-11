import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators
        

class TestAutorization:
    
    def test_enter_button_through_lk(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "/login")
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_to_be, "https://stellarburgers.nomoreparties.site/")
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'
        
    def test_enter_button_through_formregistration(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        browser.find_element(*MainLocators.BUTTON_REGISTRAION).click()
        browser.find_element(*RegPage.BUTTON_ENTER_FORMREG).click()
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_to_be, "https://stellarburgers.nomoreparties.site/")
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'
        
    def test_enter_button_through_from_recoveryform(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        browser.find_element(*MainLocators.BUTTON_REGISTRAION).click()
        browser.find_element(*RegPage.BUTTON_ENTER_RECOVERYFORM).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_to_be, "https://stellarburgers.nomoreparties.site/forgot-password")
        browser.find_element(*RegPage.BUTTON_ENTER_FOGOTPASS).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_to_be, "https://stellarburgers.nomoreparties.site/login")
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("test12345")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_to_be, "https://stellarburgers.nomoreparties.site/")
        assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'