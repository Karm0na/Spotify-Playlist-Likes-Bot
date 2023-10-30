from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import functions
import random

driver = webdriver.Firefox()
driver.get("https://10minutemail.net/")
sleep(2)

i=0

while True:
    sleep(2)    
    email = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//input[@id='fe_text']"))).get_attribute('value')

    contrasenya = (functions.randomWord()+str(random.randint(100,1000)))

    with open('contrasenyas.txt', 'a') as archivo:
        archivo.write(email+" "+contrasenya+"\n")

    sleep(2)

    driver.get("https://www.spotify.com/es/signup?forward_url=https%3A%2F%2Fopen.spotify.com%2Fintl-es")
    if i==0:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
                (By.XPATH,
        "//button[@id='onetrust-accept-btn-handler']"))).click()

    sleep(2)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//input[@id='username']"))).send_keys(email)

    sleep(2)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//button[@data-testid='submit']"))).click()

    sleep(2)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//input[@id='new-password']"))).send_keys(contrasenya)

    sleep(2)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//button[@data-testid='submit']"))).click()

    sleep(2)

    username=functions.randomWord()
    dia=random.randint(1,28)
    mes=random.randint(1,12)
    ano=random.randint(1990,2004)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//input[@id='displayName']"))).send_keys(username)

    sleep(1)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//input[@id='day']"))).send_keys(dia)

    sleep(1)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//select[@id='month']"))).click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//option[@value='"+str(mes)+"']"))).click()

    sleep(1)

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//input[@id='year']"))).send_keys(ano)

    sleep(1)
    
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//label[@for='gender_option_male']"))).click()

    sleep(1)
    
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//button[@data-testid='submit']"))).click()

    sleep(1)
    
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//button[@data-testid='submit']"))).click()

    sleep(10)

    driver.get("Your Spotify playlist link")

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//figure[@data-testid='user-widget-avatar']"))).click()

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH,
    "//button[@data-testid='user-widget-dropdown-logout']"))).click()

    driver.get("https://10minutemail.net/new.html")

    sleep(300)
    
    i=i+1
