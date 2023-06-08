import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://platform.verbit.co/"
URL_2 = "https://platform.verbit.co/?"
URL_3 = "https://platform.verbit.co/transcription_jobs/ZXlKaGJHY2lPaUpTVXpJMU5pSjkuZXlKcWIySmZhV1FpT2pVMk1qa3hOek16TENKMWMyVnlYMmxrSWpveE16YzJOako5LjJDZ2tJeFNJT1pUMHlveWxyRHZET1dVbUdhMmhQYUlvUjl3Tkd5NDg5WmdQZEh3TDEtbDNCYlNkUEdXTnNadjgzbE0xaGNMZTZEeVZSYlhoMkhXa2FHQWhtcUVsWl9sMHAwX3ZVN0xtUmdjZ1JhbGx3VWxxTXJpSElGaXMzZmN4MVFmcEc1eU1UclByQjhoMmtDa0hZUWxjdjQ5amZQLTFJVHNlZHg5NFAzX2x3RExsQXB0WEgyQlRLV1YwNmMta3hWdjNJTVVMOXVDekJ4cE1rQUg1a0Y2UmZuZDk3emxRd3E0VjZNTXc2dkttX1Z0czdUQTZaRkN2N2N4cXJ5V0FwemFETXZXSEJtLWI1VFVaVU5WYWdMM1JxWUxqNUd0N3pNcnZrS1hkV0ttUzZ4RUtOYzB6enZSWEFUbkV4OUpUS2lqV3Q1ZWphU2p2RVNqSVp2UTZ2dw==/edit"
MIN_INTERVAL = 2
MAX_INTERVAL = 3
CURRENT_URLS = [URL, URL_2, URL_3]
RELOAD_PAGE = True

def should_reload_page(current_url):
    if current_url not in CURRENT_URLS:
        return False
    else:
        return True


def login_page():
    PATH = r"/home/novek/Downloads/chromedriver_linux64/chromedriver"
    """     options = uc.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.binary_location = PATH  # Set the binary location instead of executable_path
    """

    options = uc.ChromeOptions()
    options.add_argument("--disable-popup-blocking")

    browser = uc.Chrome(executable_path=PATH, options=options)

    browser = uc.Chrome(options=options)
    base_url = "https://users.verbit.co/"
    browser.get(base_url)
    print("https://users.verbit.co/")

    email_field = browser.find_element(By.XPATH, "//input[@name='email']")
    email_field.send_keys("hannahcora22@gmail.com")

    next_button = browser.find_element(By.XPATH, "//button[contains(@class, 'sc-iwjdpV') and text()='Next']")
    next_button.click()
    time.sleep(5)

    password_field = browser.find_element(By.XPATH, "//input[@tabindex='2' and @type='password']")
    password_field.send_keys("@Rocket22")

    login_button = browser.find_element(By.XPATH, "//button[contains(@class, 'sc-iwjdpV') and text()='Login']")
    login_button.click()
    time.sleep(5)

    return browser


def locate_and_click_element(browser):
    
            try:
                # from selenium.webdriver.common.action_chains import ActionChains

                # Find all the URL elements with text "25 ¢/min"
                url_elements = browser.find_elements(By.XPATH, '//td[contains(.,"25 ¢/min")]/a')

                # Iterate over the elements
                for url_element in url_elements:
                    # Scroll to the element to ensure it's in view
                    browser.execute_script("arguments[0].scrollIntoView();", url_element)

                    # Perform visible clicking action
                    action_chains = ActionChains(browser)
                    action_chains.move_to_element(url_element).click().perform()

                    # Open the URL in a new tab
                    browser.execute_script("window.open(arguments[0], '_blank');", url_element.get_attribute("href"))

                # Switch back to the main tab
                if len(browser.window_handles) > 1:
                    browser.switch_to.window(browser.window_handles[-1])
                    time.sleep(2) 
                    browser.switch_to.window(browser.window_handles[0])
                
            except:
                print

def refresh_page(browser):
    while True:
        interval = 1.02 + random.uniform(0, 1)
        
        try:
            
            current_url = browser.current_url
            if should_reload_page(current_url):
                browser.refresh()
            # Check if the request limit content is displayed
            request_limit_element = browser.find_elements(By.XPATH, "//div[contains(@class, 'request-limit__content')]")
            if request_limit_element:
                # Pause refreshing for 15-24 seconds
                pause_duration = 16 + random.uniform(0, 9)
                round_pause_duration = round(pause_duration, 3)
                print(f"Automated tool message interception..waiting....{round_pause_duration} sec.")
                time.sleep(pause_duration)

                # Click the "Ok, got it" button to dismiss the request limit notification
                ok_button = browser.find_element(By.ID, "request_limit_back")
                browser.execute_script("arguments[0].click();", ok_button)
                print("Request limit dismissed")

                # Wait for the page to load after dismissing the request limit notification
                wait = WebDriverWait(browser, 10)
                wait.until(EC.staleness_of(request_limit_element[0]))

        except:
          PermissionError

        try:
            locate_and_click_element(browser)
            wait = WebDriverWait(browser, 4)
            browser.execute_cdp_cmd("Page.setInterceptFileChooserDialog", {"enabled": True})
            browser.switch_to.window(browser.window_handles[-1])

        except:
            print

        # Get the current URL and check if it's in the default URLs
       
        time.sleep(interval)

browser = login_page()

# Define the list of default URLs

refresh_page(browser)
browser.quit()