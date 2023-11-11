from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def login_tc(username, password):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("http://182.163.99.86/login")

    driver.implicitly_wait(10)

    username_input = driver.find_element(By.NAME, value='username')
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")

    # Enter username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Click the login button

    login_button.click()

    success_element = driver.find_element(By.CSS_SELECTOR, value=".tw-m-0.tw-mb-6.tw-text-zinc-800.tw-font-bold")
    assert success_element.text == "Dashboard"

# login_tc("admin@gigatech.com", "Abc@123")
# login_tc("farhan.omi@northsouth.edu", "Abc@123")
# login_tc("", "Abc@123")
# login_tc("admin@gigatech.com", "")
# login_tc("", "")


def logout_tc():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("http://182.163.99.86/login")

    driver.implicitly_wait(10)

    username_input = driver.find_element(By.NAME, value='username')
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/form/button")

    # Enter username and password
    username_input.send_keys("admin@gigatech.com")
    password_input.send_keys("Abc@123")

    # Click the login button

    login_button.click()

    success_element = driver.find_element(By.CSS_SELECTOR, value=".tw-m-0.tw-mb-6.tw-text-zinc-800.tw-font-bold")
    assert success_element.text == "Dashboard"

    driver.implicitly_wait(10)

    user_button = driver.find_element(By.XPATH, value="/html/body/div/section/main/div[2]/div[1]/nav/div/button")
    user_button.click()

    driver.implicitly_wait(10)

    logout_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div")
    logout_button.click()

    driver.implicitly_wait(5)
    landing_page_element = driver.find_element(By.CSS_SELECTOR, value=".tw-mt-10.tw-text-center.tw-text-2xl.tw-font-bold.tw-leading-9.tw-tracking-tight")
    assert landing_page_element.text == "Label Hub"


logout_tc()
