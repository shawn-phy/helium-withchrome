from selenium import webdriver
# https://Site.google.com//Chromium.org/chrome
PATH = r"C:\Program files (x86)\chromedriver.exe"
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

service = webdriver.chrome.service.Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://verbit.ai/")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
signin_button = driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]")


driver.get("https://verbit.ai/jobs")

driver.refresh(5)
driver.close(40)
