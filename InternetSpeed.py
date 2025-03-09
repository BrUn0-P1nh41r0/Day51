import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self, chrome_option, speed_test_driver_path, promised_down, promised_up):
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.get(speed_test_driver_path)
        self.up = ""
        self.down = ""
        self.up_value = 0
        self.down_value = 0
        self.promised_down = promised_down
        self.promised_up = promised_up

    def get_internet_speed(self):
        #Deal with cookies
        cookie = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        cookie.send_keys(Keys.ENTER)

        #Click on go button
        start_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        start_button.click()
        time.sleep(45)

        #Get values for download and upload
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

        self.up_value = self.up.text
        self.down_value = self.down.text

        #Print values for download and upload
        print(f"Down: {self.down.text}")
        print(f"Up: {self.up.text}")

    def tweet_at_provider(self, x_driver_path, twitter_username, twitter_password):
        self.driver.get(x_driver_path)
        time.sleep(5)

        #Deal with cookies
        accept_cookies = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]')
        accept_cookies.click()

        #Click on sign in and enter the account
        sign_in_button = self.driver.find_element(By.LINK_TEXT, value="Sign in")
        sign_in_button.click()
        time.sleep(5)
        #Enter email and go to the password
        email = self.driver.find_element(By.TAG_NAME, value="input")
        email.send_keys(twitter_username, Keys.ENTER)
        time.sleep(5)
        #Enter password
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(twitter_password, Keys.ENTER)

        input("Click enter when captcha complete!")

        #Tweet
        if float(self.up_value) < self.promised_up or float(self.down_value) < self.promised_down:
            tweet = self.driver.find_element(By.CLASS_NAME, value="public-DraftStyleDefault-block")
            tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down_value} down/{self.up_value} up when I pay for {self.promised_down} down/{self.promised_up} up",Keys.CONTROL, Keys.ENTER)
            tweet_send =self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
            tweet_send.click()