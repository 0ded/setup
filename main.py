from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()

prefs = {"download.default_directory" : "<C:\Program Files\programInstaller test>",
         "download.prompt_for_download" : False,
         "download.extensions_to_open" : "application/xml",
         "safebrowsing.enabled" : True}

options.add_experimental_option("prefs", prefs)
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("safebrowsing-disable-extension-blacklist")

driver = webdriver.Chrome(service= Service("C:\Program Files\chromedriver"),options=options)

try:
    driver.get("https://store.steampowered.com/about/")
    # got = driver.find_element(By.ID,value='accept-cookie-notification')
    # got.click()
    download = driver.find_element(By.XPATH, value= '//*[@id="about_greeting"]/div[4]/div[1]/a')
    download.click()
    time.sleep(5)
    driver.close()

except:
    print("Invalid URL")

