import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome();
browser.implicitly_wait(12)

browser.get("https://chercher.tech/practice/implicit-wait-example");
browser.maximize_window()

checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()
