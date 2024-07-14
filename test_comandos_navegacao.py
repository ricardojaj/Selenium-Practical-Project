import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome();

#get()
browser.get("https://www.selenium.dev/selenium/web/web-form.html");
time.sleep(2)

#maximize_window()
browser.maximize_window()

#refresh
browser.refresh()
time.sleep(5)

browser.get("https://www.google.com.br")
time.sleep(3);

#back
browser.back();
