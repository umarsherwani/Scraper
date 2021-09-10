import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://www.instagram.com")
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
password.clear()

'''enter username and password'''
username.send_keys("")
password.send_keys("")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable
                                        ((By.CSS_SELECTOR, "button[type='submit']"))).click()
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable
                                        ((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable
                                         ((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
n_scrolls = 5
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.get_screenshot_as_file(os.getcwd()+'/'+f'screenshot{j}.png')
    time.sleep(10) # add delay in the execution of a program
    driver.quit()
