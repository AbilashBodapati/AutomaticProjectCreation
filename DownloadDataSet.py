'''
    File Name: DownloadDataSet.py
    Author: Abilash Bodapati
    Version: 20200617
    Description: 
        This is a Python class that downloads the 
        dataset only from Kaggle and moves the
        unziped files from the download folder to
        the Datasets Folder in the new datascience
        juypter notebook project.
'''

# Import the packages to interact with the chrome browser
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class DownloadDataSet:
    def construct(self):
        # Use the executable file in my desktop to start the chromedriver
        self.service = Service('/home/abilashbodapati/Desktop/chromedriver')
        # Start the chromedriver service
        self.service.start()
        # Target web-url initialized (Github login-page)
        self.driver = webdriver.Remote(self.service.service_url)

    def startChromeService(self, url):
        # Use the executable file in my desktop to start the chromedriver
        # service = Service('/home/abilashbodapati/Desktop/chromedriver')

        # Start the chromedriver service
        # self.service.start()

        # Target web-url initialized (Github login-page)
        # driver = webdriver.Remote(service.service_url)
        self.driver.get(url)
        # Maximize the window when the webpage is opened
        self.driver.maximize_window()

    def downloadData(self):
        # By now we are in the webpage for dataset

        # Click on the Download button
        self.driver.find_element_by_xpath("/html/body/main/div[1]/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a[1]/div/span").click()
        time.sleep(4)

        # Click on the Signin button
        self.driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div/div[1]/a/li").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys('bodapatiabilash98@gmail.com')
        time.sleep(20)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/span/span").click()
        time.sleep(35)

        

        # Click on the Download button again after signed in
        self.driver.find_element_by_xpath("/html/body/main/div[1]/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a[1]/div/span").click()
        time.sleep(1.75)

    def moveDataToFolder(self):
        # Unzip the folder from Downloads to Datasets folder.
        os.system('unzip -q /home/abilashbodapati/Downloads/*_bundle_archive.zip -d ./Datasets')

