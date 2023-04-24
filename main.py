import requests
import os
import sys
import json
import cloudscraper

global config 
##global daily_case = "https://csgocases.com/case/daily-free"
##global request_module = requests

def create_config():
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
        print(config)

create_config()