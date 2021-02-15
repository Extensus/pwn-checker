from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cryptocode


# DECRYPTION KEY
decrypt_key = '#314159265358979323'


def get_pass_from_base():
    with open('datainfo.txt', 'r+') as f:
        content = f.readlines()
        raw_password = cryptocode.decode(decrypt_key, content[0])
        raw_email = cryptocode.decode(decrypt_key, content[0])
        return {email_1: raw_email, pass_1:raw_password}


def enter_passes_to_base():
    with open('datainfo.txt', 'w') as f:
        password = cryptocode.encrypt(decrypt_key, raw_password)
        email = cryptocode.encrypt(decrypt_key, raw_email)
        f.write(password + "\n")
        f.write(email + "\n")


# VARIABLES
pass_dict = get_pass_from_base()
raw_email =

CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application'
CHROMEDRIVER_PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
WINDOW_SIZE = "1920,1080"


# STARTING DRIVER
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://haveibeenpwned.com/")

with open('datainfo.txt', 'w') as f:
    password = cryptocode.encrypt(raw_password)
    email = cryptocode.encrypt(raw_email)
    f.write(password + "\n")
    f.write(email + "\n")


def wait(num):
    time.sleep(num)


def get_email_pwn():
    password_button = driver.find_element_by_link_text("Home")
    password_button.click()
    search_box = driver.find_element_by_class_name("form-control")
    search_box.send_keys(raw_email)
    search_box.send_keys(Keys.ENTER)
    wait(2)
    driver.get_screenshot_as_file('capture_email.png')
    result_email = driver.find_element_by_class_name("pwnTitle").get_attribute("innerText")
    return result_email


def get_pass_pwn():
    password_button = driver.find_element_by_link_text("Passwords")
    password_button.click()
    search_box = driver.find_element_by_class_name("form-control")
    search_box.send_keys(raw_password)
    search_box.send_keys(Keys.ENTER)
    wait(2)
    driver.get_screenshot_as_file('capture_pass.png')
    result_password = driver.find_element_by_id("pwnedPasswordResult").get_attribute("innerText")
    return result_password


print(get_email_pwn())
print(get_pass_pwn())


driver.quit()
