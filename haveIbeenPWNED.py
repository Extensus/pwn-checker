from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import cryptocode

# DECRYPTION KEY
decrypt_key = '#314159265358979323'

# VARIABLE DECLARATION
raw_email = ""
raw_password = ""


def get_pass_from_base(txt):
    with open('datainfo.txt', 'r+') as f:
        content = f.readlines()
        print(content)
        r_password = cryptocode.decrypt(decrypt_key, content[0])
        r_email = cryptocode.decrypt(decrypt_key, content[0])
        if txt == 'raw_email':
            return r_email
        elif txt == "raw_password":
            return r_password
        else:
            pass


def enter_passes_to_base():
    with open('datainfo.txt', 'w') as f:
        password = cryptocode.encrypt(decrypt_key, raw_password)
        email = cryptocode.encrypt(decrypt_key, raw_email)
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


##########################################################

CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application'
CHROMEDRIVER_PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
WINDOW_SIZE = "1920,1080"
# STARTING DRIVER
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get("https://haveibeenpwned.com/")


# GET STUFF FROM BASE
raw_password = get_pass_from_base("raw_password")
raw_email = get_pass_from_base("raw_email")

driver.quit()
