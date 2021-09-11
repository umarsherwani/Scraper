import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

'''Open The Webpage'''
driver.get("http://www.instagram.com")

'''Instagram Login function that takes two arguments Username & Password'''
def instalogin(username,password):

    '''Open The Webpage'''
    driver.get("http://www.instagram.com")
    
    UserName = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    PassWord = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    UserName.clear()
    PassWord.clear()
    UserName.send_keys(username)
    PassWord.send_keys(password)

    '''Target the login button'''
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

    '''Screenshot'''
    driver.get_screenshot_as_file('Screenshot.png')

'''Please Pass the arguments'''
instalogin(username = input("Enter Username: "),password = input("Enter password: "))
