import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators

class TestChangePlace:
    
    def test_changeplace_click_on_button_lk(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "/login")
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        browser.find_element(*MainLocators.BUTTON_LOGIN_LK).click()
        assert browser.current  == 'https://stellarburgers.nomoreparties.site/'
        
    def test_changeplace_click_on_construktor(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        browser.find_element(*MainLocators.BUTTON_CONSTRUKTOR).click()
        assert browser.current  == 'https://stellarburgers.nomoreparties.site/'
        
    def test_changeplace_click_on_logoSB(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegPage.BUTTON_ENTER_IN_ACC).click()
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        browser.find_element(*RegPage.BUTTON_NAME).send_keys("testtesttesttes@gmail.com")
        browser.find_element(*RegPage.BUTTON_EMAIL).send_keys("testtest")
        browser.find_element(*RegPage.BUTTON_LOGIN).click()
        browser.find_element(*MainLocators.LOGO).click()
        assert browser.current  == 'https://stellarburgers.nomoreparties.site/'
