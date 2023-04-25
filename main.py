import time
import requests
import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def main_process():
    options = uc.ChromeOptions()
    options.user_data_dir = "C:/Users/Andrew/AppData/Local/Google/Chrome/User Data"
    options.add_argument("profile-directory=Profile 1")
    driver = uc.Chrome(options=options)

    driver.get("https://csgocases.com/case/ez-1-100-profit")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "lotteryStart"))
    )

    case = driver.find_element(By.TAG_NAME, 'h1').text
    thumbnail = driver.find_element(By.CLASS_NAME, 'case-img').get_attribute("src")
    
    driver.find_element(By.CLASS_NAME, "case-test-button").click()
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h1[@class='ng-scope']//span[1]"))
    )

    reward = driver.find_element(By.XPATH, "//h1[@class='ng-scope']//span[1]").text

    
    send_webhook(case, reward, thumbnail)


def send_webhook(case, reward, thumbnail):
    webhook_url = "https://discord.com/api/webhooks/1004215996908843060/hAbD6iuAl1_qHUkjHJxAWyhkulX5AYrwS3abvSXSPCsW7pivUeKYFB6GkFNtrigwswKv"

    data = {
        "embeds": [
            {
                "title": f'Case Opened: {case}',
                "url": "https://csgocases.com/r/u70633zei",
                "color": 16774400,
                "fields": [
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

    requests.post(webhook_url, json=data)

main_process()
