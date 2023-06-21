from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
# import logging

# Set the logging level to ignore or suppress Selenium errors
# logging.getLogger('selenium').setLevel(logging.WARNING)




# Works on : LinkedIn: Log In or Sign Up
def get_notification_and_messages(email, login_password):
    driver_path = "C:\\Users\\svsma\\OneDrive\\Desktop\\environments\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    url = 'https://linkedin.com'
    driver.get(url)
    while driver.title!= "LinkedIn: Log In or Sign Up":
        driver.get(url)
        print("Opening LinkedIN")
 
    print("Succesfully Loaded Linkedin")

    # Get username and password input boxes path
    username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
    password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
    print("Found login boxes")

    # Input the email id and password
    username.send_keys(email)
    password.send_keys(login_password)
    print("entered details")


    # Click the login button
    login_btn = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
    login_btn.click()
    print("Logged in succesfully!!")
    print("Now on :", driver.title)
    if driver.title == "Security Verification | LinkedIn" :
        print("Please complete captcha")
        sleep(10)
    sleep(3)
    try:
        number_of_messages = driver.find_element(By.XPATH, '//*[@id="ember13"]/span/span[1]')
        print("Messages: ",number_of_messages.text)
        messages= number_of_messages.text
    except:
        messages = 0
        print("Messages: ",messages)
    try :        
        number_of_notification = driver.find_element(By.XPATH, '//*[@id="ember12"]/span/span[1]')
        notifs = number_of_notification.text
        print("Notifications: ",number_of_notification.text)
    except :
        notifs = 0 
        print("Notifications: ",notifs)

    
    driver.quit()

    return messages, notifs