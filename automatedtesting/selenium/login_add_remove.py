# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


# Start the browser and login with standard_user
def login (user, password):
    logging.info('Starting the browser...')
    CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--remote-debugging-pipe')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options )
    #driver = webdriver.Chrome()
    logging.info('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    
    logging.info('Loggig in ..')
    driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()
    time.sleep(1) 
    
    url_after_login = "https://www.saucedemo.com/inventory.html" 
    logging.info(driver.current_url)
    
    assert driver.current_url in url_after_login
    
    logging.info("Testing adding to cart")
    add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")

    # Click six buttons to make the cart_value 6
    for btns in add_to_cart_btns[:6]:
        logging.info(btns.get_attribute("name"))
        btns.click()       
    time.sleep(1)
    
    # Check cart value to be 6 
    cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert "6" in cart_value.text
    time.sleep(1)
    
    logging.info("Testing remove items from cart")
    remove_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btns in remove_btns[:6]:      
        logging.info(btns.get_attribute("name"))
        btns.click()
    time.sleep(1)
        
     
login('standard_user', 'secret_sauce')

