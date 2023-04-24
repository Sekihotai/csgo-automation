import requests
import os.path
import json
import cloudscraper

config = {
    "cookie": "",
    "delay": 0
}
config_json = "config.json"
daily_case = "https://csgocases.com/case/daily-free"
request_module = requests

if os.path.isfile(config_json) != True:
    ws = open(config_json, "w")
    config["cookie"] = input("Paste in the login cookie")
    ws.write(json.dumps(config))
    ws.close()

    rs = open(config_json, "r")
    config = json.loads(rs.read())
else: 
    config = json.loads(open("config.json", "r").read())
    print(config)
