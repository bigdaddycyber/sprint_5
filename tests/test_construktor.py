import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators

class TestConstruktor:
    
    def test_navigate_tab_bulki(browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.finnd_element(*MainLocators.BULKA).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "https://stellarburgers.nomoreparties.site")
        bulki_tab = browser.find_element(By.CLASS_NAME, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')
        assert bulki_tab == 'Булки'

    def test_navigate_tab_souse(browser):  
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_elemen(*MainLocators.SOUCE).click
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "https://stellarburgers.nomoreparties.site")
        souse_tab = browser.find_element(By.CLASS_NAME, 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect')
        assert souse_tab == "Соусы"
        
    def test_navigate_tab_nachinka(browser):    
        browser.find_element(*MainLocators.NACHINKA).click()
        WebDriverWait(browser, timeout=3).until(expected_conditions.url_contains, "https://stellarburgers.nomoreparties.site")
        nachinka_tab = browser.find_element(*By.CLASS_NAME, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')
        assert nachinka_tab == "Начинки"
       


