import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.saucedemo.com/")

print("Titulo pagina: ", browser.title)

print("URL: ", browser.current_url)

print("Codigo Fonte: ", browser.page_source)
