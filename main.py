from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


YOUR_USERNAME = "username"
YOUR_PASSWORD = "password"

user = input("Enter the user whose followers you want to follow: ")
user_to_look_at = f"https://poshmark.com/closet/{user}"
chrome_driver_path = Service("path/to/your/chromedriver")

driver = webdriver.Chrome(service=chrome_driver_path)
POSHMARK_URL = "https://poshmark.com"

driver.get(POSHMARK_URL)
login = driver.find_element(By.CSS_SELECTOR, ".tc--lb")
login.click()
time.sleep(2)
username_field = driver.find_element(By.ID, "login_form_username_email")
username_field.send_keys(YOUR_USERNAME)
password_field = driver.find_element(By.ID, "login_form_password")
password_field.send_keys(YOUR_PASSWORD)
password_field.send_keys(Keys.RETURN)
time.sleep(3)
driver.get(user_to_look_at)

time.sleep(1)
followers = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/div[2]/div/div[2]/nav/ul/li[3]/div')
followers.click()
time.sleep(2)

scroll_down = driver.find_element(By.ID, "app")
follow_buttons = driver.find_elements(By.CLASS_NAME, "follow__btn")

# add one for user input
for button in follow_buttons[:12]:
    time.sleep(1)
    if button.text == "Follow":
        button.click()



