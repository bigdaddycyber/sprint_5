import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators

class TestChangePlace:
    
    def test_changeplace_click_on_button_lk(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        driver.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        assert driver.find_element(*MainLocators.BUTTON_ORDER)
        
    def test_changeplace_click_on_construktor(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        driver.find_element(*MainLocators.BUTTON_CONSTRUKTOR).click()
        assert driver.find_element(*MainLocators.BUTTON_ORDER)
        
    def test_changeplace_click_on_logoSB(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        driver.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        driver.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        driver.find_element(*RegPage.BUTTON_LOGIN).click()
        driver.find_element(*MainLocators.LOGO).click()
        assert MainLocators.MAIN_PAGE
    
