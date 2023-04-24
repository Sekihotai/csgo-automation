import requests
import os.path
import json
import cloudscraper

config = {
    "cookie": "",
    "delay": 0
}
daily_case = "https://csgocases.com/case/daily-free"
request_module = requests


#r = request_module.get("https://csgocases.com/")

# if "href" in r.text:
#     print("yes")
# else:
#     print("no")

#if "challenge-error-text" in r.text:
    #request_module = cloudscraper.create_scraper()

if os.path.isfile("config.json") != True:
    config["cookie"] = input("Paste in the login cookie")
    open("config.json", "w").write(json.dumps(config))
else: 
    config = json.loads(open("config.json", "r").read())
    print(config)
