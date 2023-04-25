import time
import requests
import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def main_process():
    # name_case = "https://csgocases.com/case/daily-free"
    # avatar_case = "https://csgocases.com/case/daily-free-2"
    def webdriver_setup():
        options = uc.ChromeOptions()
        options.user_data_dir = "C:/Users/Andrew/AppData/Local/Google/Chrome/User Data"
        options.add_argument("profile-directory=Profile 1")
        driver = uc.Chrome(options=options)

    def open_cases():
        

    
    driver.get("https://csgocases.com/case/ez-1-100-profit")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "lotteryStart"))
    )
    # normal cases is lotteryStart and is found By.ID
    driver.find_element(By.CLASS_NAME, "case-test-button").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[@class='ng-scope']//span[1]"))
    )
    reward = driver.find_element(By.XPATH, "//h1[@class='ng-scope']//span[1]")
    send_webhook("", reward, "", "")
    time.sleep(120)

def send_webhook(case, reward, status, thumbnail):
    webhook_url = "https://discord.com/api/webhooks/1004215996908843060/hAbD6iuAl1_qHUkjHJxAWyhkulX5AYrwS3abvSXSPCsW7pivUeKYFB6GkFNtrigwswKv"

    data = {
        "content": null,
        "embeds": [
        {
            "title": case,
            "url": "https://csgocases.com/r/u70633zei",
            "color": 16774400,
            "fields": [
                        {
                            "name": "Status",
                            "value": status
                        },
                        {
                            "name": "Reward",
                            "value": reward
                        }
                    ],
            "footer": {
                "text": "spiritual is stupid"
            },
      "timestamp": "2023-04-11T19:23:00.000Z",
      "thumbnail": {
        "url": thumbnail
        }
        }
        ],
        "attachments": []
    }




    




main_process()
