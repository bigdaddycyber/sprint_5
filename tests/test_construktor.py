import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegPage, MainLocators

class TestConstruktor:
    
    def test_navigate_tab_bulki_souce_nachinka(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, timeout=3).until(expected_conditions.url_contains, "/login")
        active_tab = driver.find_element(*MainLocators.BULKA).text
        assert active_tab == 'Булки'
        driver.find_element(*MainLocators.SOUCE).click()
        new_tab = driver.find_element(*MainLocators.SOUCE).text
        assert new_tab == "Соусы"
        driver.find_element(*MainLocators.NACHINKA).click()
        new_tab_next = driver.find_element(*MainLocators.NACHINKA).text
        assert new_tab_next == "Начинки"
