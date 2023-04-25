import time
import undetected_chromedriver as uc
from selenium.webdriver.remote.webdriver import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def open_cases():
    # name_case = "https://csgocases.com/case/daily-free"
    # avatar_case = "https://csgocases.com/case/daily-free-2"
    options = uc.ChromeOptions()
    options.user_data_dir = "C:/Users/Andrew/AppData/Local/Google/Chrome/User Data"
    options.add_argument("profile-directory=Profile 1")
    driver = uc.Chrome(options=options)
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
    print(reward.text)
    time.sleep(120)

def send_webhook():
    




open_cases()
