from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



def validation_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("http://182.163.99.86/login")

    driver.implicitly_wait(10)

    username_input = driver.find_element(By.NAME, value='username')
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")

    # Enter username and password
    username_input.send_keys("w@q.com")
    password_input.send_keys("Abc@123")

    # Click the login button

    login_button.click()

    success_element = driver.find_element(By.CSS_SELECTOR, value=".tw-m-0.tw-mb-6.tw-text-zinc-800.tw-font-bold")
    assert success_element.text == "Dashboard"

    driver.implicitly_wait(10)

    projects_button = driver.find_element(By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[2]/a/div")
    projects_button.click()

    time.sleep(5)

    view_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody/tr/td[9]/div/a")
    view_button.click()

    time.sleep(5)

    start_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a")
    start_button.click()

    time.sleep(3)

    like_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[1]/button")
    like_button.click()

    time.sleep(5)

    edit_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[2]/div/div[2]")
    edit_button.click()

    time.sleep(2)

    reject_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[2]")
    reject_button.click()




validation_test()


