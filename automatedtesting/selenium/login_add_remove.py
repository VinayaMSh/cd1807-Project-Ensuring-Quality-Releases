# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--remote-debugging-pipe')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options )
    #driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    
    print ('Loggig in ..')
    driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()
    time.sleep(1) 
    
    url_after_login = "https://www.saucedemo.com/inventory.html" 
    print(driver.current_url)
    
    assert driver.current_url in url_after_login
    
    print ('Adding Sauce Labs Backpack to cart')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']").click()
    time.sleep(1)
    
    print ('Removing item from cart')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-backpack']").click()
    time.sleep(1)
    
    
login('standard_user', 'secret_sauce')

