import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options



def comecar():

    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    time.sleep(25)


