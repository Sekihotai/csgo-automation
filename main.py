import requests
import os, sys
import json
import cfscrape

global config 
global request


def create_config():
    global config 
    config = {
        "cookie": "",
        "delay": 0
    }
        
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


def check_for_cloudflare():
    global request
    request = requests
    r = request.get("https://csgocases.com/")
    if "Enable JavaScript and cookies to continue" in r.text:
        request = cfscrape.create_scraper()

def open_cases():
    name_case = "https://csgocases.com/case/daily-free"
    avatar_case = "https://csgocases.com/case/daily-free-2"
    cookies = dict(symfocms = config["cookie"])

    r = request.get(name_case, cookies=cookies)
    print(r.text)

create_config()
check_for_cloudflare()    
open_cases()
