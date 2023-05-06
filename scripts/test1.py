from helium import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.chrome()

start_chrome('https://users.verbit.co/')
write('michaeldamian935@gmail.com', into='email')
click('next')
write('Alfie9080*', into = 'password')
click('login')

for i in range(10): # Refresh the page 10 times
	webdriver.implicitly_wait(2)
	webdriver.refresh()


