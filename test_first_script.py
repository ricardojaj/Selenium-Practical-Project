import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome();

#get()
browser.get("https://www.selenium.dev/selenium/web/web-form.html");
time.sleep(2)


fieldTitle = browser.find_element(By.CLASS_NAME, "display-6")
print(fieldTitle.text)

fieldText = browser.find_element(By.ID, "my-text-id");
fieldText.send_keys('Novo Teste');
time.sleep(5);


submit_button_lotator = browser.find_element(By.XPATH, "//button[@class='btn btn-outline-primary mt-3']");
submit_button_lotator.click()
time.sleep(2)
