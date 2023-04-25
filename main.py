import os, sys
import time
import undetected_chromedriver as uc

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC  
from selenium.webdriver.support.wait import WebDriverWait

cookie = ""

def create_config():
    global cookie

    def read_cookie():
        rs = open("cookie.dat", "r")
        cookie = rs.read()
        print(cookie)
        rs.close()

    if os.path.isfile("cookie.dat") != True:
        cookie = input("Please paste in the login cookie: ")
        if cookie != "":
            ws = open("cookie.dat", "w")
            ws.write(cookie)
            ws.close()
        else:
            cookie = input("Cookie cannot be empty. Please paste in the login cookie: ")
    else: 
        read_cookie()
        

def open_cases():
    # global config
    # name_case = "https://csgocases.com/case/daily-free"
    # avatar_case = "https://csgocases.com/case/daily-free-2"
    # cookies = dict(symfocms = config["symfocms"])
    driver = uc.Chrome()
    driver.get("https://csgocases.com")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button-case")) 
    )
    driver.delete_cookie("symfocms")
    driver.add_cookie({"name" : "symfocms", "path" : "/", "sameSite" : "Lax", "domain" : "csgocases.com", "value" : cookie})
    driver.refresh()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "button-case")) 
    )
    print(driver.get_cookies())
    driver.save_screenshot("lol.png")
    driver.quit()
 
create_config()
open_cases()
