# helium-withchrome
this is a repository of the random scripts i write for automating tasks on various websites

### day 2 
fixed issues with chromedriver amd chrome versioning not being the same

at the same time had another error 
``` shell 
Traceback (most recent call last):
  File "C:\Users\shawn-phy\Documents\github\helium-withchrome\scripts\test1.py", line 9, in <module>
    driver = webdriver.Chrome()
             ^^^^^^^^^^^^^^^^^^
  File "C:\Users\shawn-phy\Documents\github\helium-withchrome\venv\Lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 73, in __init__
    self.service.start()
  File "C:\Users\shawn-phy\Documents\github\helium-withchrome\venv\Lib\site-packages\selenium\webdriver\common\service.py", line 81, in start
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```

### day 3 
pending import issues were solved but ``` webdriver object not responding```

#### evaluation of complexity of project 
- add a timeout detector 
- add CSS_SELECTOR for navigating to adjacent pages as they appear 
- add a dynamic implicit wait function

