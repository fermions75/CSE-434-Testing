from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# # tc 1  ---> ok
# fullname = "omifahan"
# email = "omifarhans@omiaaa.com"
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01317258981"
# role = "manager"

# # tc 2  --> ok
# fullname = "omifahans"
# email = "omifarhans@omis.com"
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Annotator"
#
# tc 3 ---> ok
# fullname = "omifahanss"
# email = "omifarhans@omiss.com"
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Validator"
#
#
# tc 4 ---> ok
# fullname = "omifahansss"
# email = "omifarhans@omisss.com"
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
# tc 5 --> ok
# fullname = ""
# email = "omifarhans@omisss.com"
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
# tc 6 ---> not showing proper error msg
# fullname = "O"
# email = ""
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
# # tc 7  ---> ok
# fullname = "Ooo"
# email = "omifarhans@omissss.com"
# #gender unselect
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
#
# # tc 8 --> ok
# fullname = "Ooo"
# email = "omifarhans@omissss.com"
# #birthday off
# inst_name = "NSU"
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
#
# tc 9  --> ok
# fullname = "Oooooo"
# email = "omifarhans@omisssssss.com"
# inst_name = ""
# qualification = "grad"
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
# # tc 10  ---> ok
# fullname = "Ooooooooo"
# email = "omifarhans@omisssssss.com"
# inst_name = ""
# qualification = ""
# password = "Abc@123"
# mobile = "01700000000"
# role = "Guest"
#
#
#
# # # tc 11  ---> unexpected result
# fullname = "Ooooooooo"
# email = "omifarhans@omisssssssss.com"
# inst_name = ""
# qualification = ""
# password = "Abc@123"
# mobile = "01317258981326658516"
# role = ""  #comment
#
#
#
#
#
#
#
#
#
# # tc 12 ---> ok
# fullname = "Omiasdasdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# email = "omifarhans@omissssssssssss.com"
# inst_name = "a"
# qualification = "s"
# password = "Abc@123"
# mobile = "01700000000"
# role = ""  #comment

# # tc 13 ---> ok
# fullname = "Omiasdasdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# email = "omifarhans@omissssssssssss.com"
# inst_name = "a"
# qualification = "s"
# password = "Abc@"
# mobile = "01700000000"
# role = ""  #comment





def add_user_test(full_name, emails, instname, qualific, passwords, mobiles):
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


    users_button = driver.find_element(By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[3]/a")
    users_button.click()

    driver.implicitly_wait(5)

    add_user_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[2]/button")
    add_user_button.click()


    # user inputs
    fullname = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/input")
    fullname.send_keys(full_name)
    time.sleep(3)

    email = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/input")
    email.send_keys(emails)
    time.sleep(3)

    click_gender_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/select/option[2]")
    click_gender_button.click()
    time.sleep(3)

    DOB = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/input")
    DOB.click()


    driver.implicitly_wait(3)

    inst_name = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[3]/input")
    inst_name.send_keys(instname)
    time.sleep(3)

    qualification = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[3]/input")
    qualification.send_keys(qualific)
    time.sleep(3)

    password = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[4]/input")
    password.send_keys(passwords)
    time.sleep(3)

    mobile = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div[4]/input")
    mobile.send_keys(mobiles)
    time.sleep(3)

    # role = manager
    # role_manager = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[5]/select/option[2]")
    # role_manager.click()

    # # role = annotator
    # role_annotator = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[5]/select/option[3]")
    # role_annotator.click()
    #
    # # role = validator
    # role_validator = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[5]/select/option[4]")
    # role_validator.click()
    #
    # # role = guest
    # role_guest = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div[5]/select/option[5]")
    # role_guest.click()


    add_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]")
    time.sleep(5)
    add_button.click()




def delete_user_test():
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

    users_button = driver.find_element(By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[3]/a")
    users_button.click()

    driver.implicitly_wait(5)

    click_delete_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div/span[3]")
    click_delete_button.click()

    time.sleep(5)

    click_yes_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")
    click_yes_button.click()

# add_user_test(fullname, email, inst_name, qualification, password, mobile)


delete_user_test()