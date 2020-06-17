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

    def DownloadData(self):
        # By now we are in the webpage for dataset

        # Click on the Download button
        self.driver.find_elements_by_xpath("/html/body/main/div[1]/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a[1]/div/span").click()
        # Click on the Signin button
        self.driver.find_elements_by_xpath("/html/body/main/div[1]/div[1]/div/form/div[2]/div/div[1]/a/li").click()
        self.driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]").click()

        # Click on the Download button again after signed in
        self.driver.find_elements_by_xpath("/html/body/main/div[1]/div/div[5]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/a[1]/div/span").click()

    def MoveDataToFolder(self):
        os.system('unzip -q /home/abilashbodapati/Downloads/*_bundle_archive.zip -d ./Datasets')

