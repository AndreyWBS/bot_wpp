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



#C:\Users\gabri\AppData\Local\Temp\scoped_dir10596_811454473\Default
#C:\Users\gabri\AppData\Local\Temp\scoped_dir2968_973316188\Default

"""
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:/Users/e5512459/AppData/Local/Google/Chrome/User Data")
self.brs = webdriver.Chrome(executable_path="C:/Users/e5512459/PycharmProjects/wpp/chromedriver.exe", chrome_options=chrome_options)
"""