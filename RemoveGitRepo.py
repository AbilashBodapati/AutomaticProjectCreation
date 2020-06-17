'''
    File Name: RemoveGitRepo.py
    Author: Abilash Bodapati
    Version: 20200617
    Description: 
        This is a Python class that uses selenium webdriver to
        interact with github and remove a repository and its
        dependency files.  
'''

# Import the packages to interact with the chrome browser
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from CreateGitRepo import CreateGitRepo

# A class that Extends the CreateGitRepo class to reuse code
class RemoveGitRepo(CreateGitRepo):
    # This class will only have one function because the other functions are inherited by class
    def removeRepo(self, projectname):
        '''
            This is the point 
            I am logged into 
            the github homepage.
        '''

        # Click on the "Show more" button. 
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/img").click()
        time.sleep(1.25)
        
        # Click on the "Your Repository" tab. 
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/a[2]").click()
        time.sleep(1)

        # Type in the Repo Name in the search bar
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div[3]/div[1]/form/div[1]/input[2]").send_keys(projectname)
        time.sleep(1)

        # Click on the repo link.
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div[3]/div[2]/div/ul/li[1]/div[1]/div[1]/h3/a").click()
        time.sleep(3)

        # Click on the Setting tab
        self.driver.find_element_by_xpath("/html/body/div[4]/div/main/div[1]/nav/ul/li[9]/a/span").click()
        time.sleep(4)

        # Click on the "Delete this Repository" tab
        self.driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[9]/ul/li[4]/details/summary").click()
        time.sleep(4)

        # Send keys to the delete repo text bar and click on the button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input").send_keys('AbilashBodapati/%s'%(projectname))
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button").click()
        time.sleep(1)
