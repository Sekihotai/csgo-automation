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


    def write_cookie():
        cookie = input("Please paste in the login cookie: ")
        ws = open("cookie.dat", "w")
        ws.write(cookie)
        ws.close()
        read_cookie()

    if os.path.isfile("cookie.dat") != True: 
        write_cookie()
    else:
        read_cookie()
            

    
        

def open_cases():
    # name_case = "https://csgocases.com/case/daily-free"
    # avatar_case = "https://csgocases.com/case/daily-free-2"
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
    driver.quit()
 
create_config()
open_cases()
