import os
import time
from selenium import webdriver
from InternetSpeed import InternetSpeedTwitterBot

PROMISED_DOWN = 500
PROMISED_UP = 10
TWITTER_USERNAME = os.environ["TWITTER_USERNAME"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option("detach", True)

speed_test_driver_path = "https://www.speedtest.net/pt"
x_driver_path = "https://www.x.com"

InternetSpeedTwitterBot = InternetSpeedTwitterBot(CHROME_OPTIONS, speed_test_driver_path, PROMISED_DOWN, PROMISED_UP)
InternetSpeedTwitterBot.get_internet_speed()
time.sleep(3)
InternetSpeedTwitterBot.tweet_at_provider(x_driver_path, TWITTER_USERNAME, TWITTER_PASSWORD)
