import requests
import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def main_process():
    def open_cases(url): 
        options = uc.ChromeOptions()
        options.user_data_dir = "C:/Users/Andrew/AppData/Local/Google/Chrome/User Data"
        options.add_argument("profile-directory=Profile 1")
        driver = uc.Chrome(options=options)


        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "lotteryStart"))
        )

        case = driver.find_element(By.TAG_NAME, 'h1').text
        thumbnail = driver.find_element(By.CLASS_NAME, 'case-img').get_attribute("src")
        
        driver.find_element((By.ID, "lotteryStart")).click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h1[@class='ng-scope']//span[1]"))
        )

        reward = driver.find_element(By.XPATH, "//h1[@class='ng-scope']//span[1]").text

        driver.quit()
        send_webhook(case, reward, thumbnail)

    open_cases("https://csgocases.com/case/daily-free")
    open_cases("https://csgocases.com/case/daily-free-2")

def send_webhook(case, reward, thumbnail):
    webhook_url = "https://canary.discord.com/api/webhooks/1100522199607164938/6sVgPu3_O8rKNCFy5KZcvAeWRVJnvDJ2xvKrbYZ6G99PQENOHhqGjQZ3qqS3gBLLjerw"

    data = {
        "embeds": [
            {
                "title": f'Case Opened: "{case}"',
                "url": "https://csgocases.com/r/u70633zei",
                "color": 16774400,
                "fields": [
                    {
                        "name": "Reward",
                        "value": reward
                    }
                ],
                 "thumbnail": {
                  "url": thumbnail
                  }
            }
        ],
        "attachments": []
    }

    requests.post(webhook_url, json=data)

main_process()
