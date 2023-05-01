from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = r"C:\Program files (x86)\chromedriver.exe"


def login_page():
    driver = webdriver.Chrome()



    driver.get("https://users.verbit.co/")


    #signin_button = driver.find_element("//a[contains(text(),'log in')]")
    #signin_button = driver.find_element()

    #signin_button.click()

    username_field = driver.find_element(By.XPATH, ) # type: ignore
    #username_field = driver.find_element(By.NAME, 'email')

    driver.implicitly_wait(5)

    username_field.send_keys("michaeldamiana935@gmail.com")

    driver.implicitly_wait(5)

    next_button = driver.find_element(By.CSS_SELECTOR, value="button")
    next_button.click()


    password_field = driver.find_element(By.XPATH, "//input[@name='Alfie9080*']") # type: ignore
    #username_field.send_keys("michaeldamiana935@gmail.com")
    #password_field.send_keys("Alfie9080*")
    #login_button = driver.find_element_by_xpath("//button[@type='submit']")
    #login_button.click()

    #driver.get("https://verbit.ai/jobs")

    #for i in range(10): # Refresh the page 10 times
    #    driver.implicitly_wait(5)
    #    time.sleep(300)
    #    driver.refresh()
    #driver.refresh()

    driver.close()

login_page()


if __name__ == "__main__":
    login_page()