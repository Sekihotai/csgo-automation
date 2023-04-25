import requests
import os, sys
import json
import time
import undetected_chromedriver as uc

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  
from selenium.webdriver.support.wait import WebDriverWait

config = {"cookie": "", "delay": 0}
request = requests

def create_config():
    global config
    if os.path.isfile("config.json") != True:
        config["cookie"] = input("Please paste in the login cookie: ")
        if config["cookie"] != "":
            ws = open("config.json", "w")
            ws.write(json.dumps(config))
            ws.close()
        else:
            os.execl(sys.executable, sys.executable, *sys.argv)
    else: 
        rs = open("config.json", "r")
        config = json.loads(rs.read())

def open_cases():
    # global config
    # global request
    # name_case = "https://csgocases.com/case/daily-free"
    # avatar_case = "https://csgocases.com/case/daily-free-2"
    # cookies = dict(symfocms = config["cookie"])
    driver = uc.Chrome()
    driver.get("https://csgocases.com")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nick-full"))
    )
    driver.save_screenshot("lol.png")
    driver.quit()
 

open_cases()
