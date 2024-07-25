from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

driver_path = r"C:\Users\DELL\Documents\Automation\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get('https://www.hindustantimes.com/')
driver.maximize_window()
time.sleep(15)
E_paper = driver.find_element(By.CSS_SELECTOR, '.epaper icon').click()

username = 'nsnandhasantha@gmail.com'
password = 'Nsnandha@9986302295'

