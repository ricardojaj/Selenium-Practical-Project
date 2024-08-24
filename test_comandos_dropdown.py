import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)


browser.get("https://www.selenium.dev/selenium/web/web-form.html")
browser.maximize_window()

dropdown = Select(browser.find_element(By.XPATH, "//select[@class='form-select']"))
dropdown.select_by_visible_text("Two")
time.sleep(5)
