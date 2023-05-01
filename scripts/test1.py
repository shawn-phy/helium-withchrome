from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


PATH = r"C:\Program Files (x86)\chromedriver.exe"


driver = webdriver.Chrome()

driver.get('https://users.verbit.co/')

