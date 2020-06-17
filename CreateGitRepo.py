'''
    File Name: CreateGitRepo.py
    Author: Abilash Bodapati
    Version: 20200617
    Description: 
        This is a Python class that uses selenium webdriver to
        interact with github and create a new repository for my
        code to be pushed into as an initial commit.  
'''

# Import the packages to interact with the chrome browser
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class CreateGitRepo:
    def construct(self, project_name, username, password):
        self.project_name = project_name
        self.username = username
        self.password = password
        
        # Use the executable file in my desktop to start the chromedriver
        self.service = Service('/home/abilashbodapati/Desktop/chromedriver')
        # Start the chromedriver service
        self.service.start()
        # Target web-url initialized (Github login-page)
        self.driver = webdriver.Remote(self.service.service_url)

    def startChromeService(self):
        # Use the executable file in my desktop to start the chromedriver
        # service = Service('/home/abilashbodapati/Desktop/chromedriver')

        # Start the chromedriver service
        # self.service.start()

        # Target web-url initialized (Github login-page)
        # driver = webdriver.Remote(service.service_url)
        self.driver.get('http://www.github.com/login')
        # Maximize the window when the webpage is opened
        self.driver.maximize_window()

    def accessGithub(self):
        '''
            This is the point 
            I am on the Github
            login page.
        '''
        # Passing username argument into login field
        self.driver.find_elements_by_xpath("//input[@name='login']")[0].send_keys(self.username)
        # Passing password argument into password field
        self.driver.find_elements_by_xpath("//input[@name='password']")[0].send_keys(self.password)
        # Once the credentials are passed in, click on the submit button
        self.driver.find_elements_by_xpath("//input[@name='commit']")[0].click()

    def createRepo(self):
        '''
            This is the point 
            I am logged into 
            the github homepage.
        '''

        # Click on the "Create new repo button." 
        self.driver.find_element_by_xpath("//a[@href='/new'][@class='btn btn-sm btn-primary text-white']").click()

        # New Repository name and Description 
        ## We will use the values from the project creation script
        # repo_name = sys.argv[1]

        # Passing the repo name provided by the input into the new Repo page
        self.driver.find_element_by_xpath("//input[@name='repository[name]']").send_keys(self.project_name)

        # Slow down the transaction
        time.sleep(2.5)

        # Once the Repo details are filled out, click on the Create Repository button.
        self.driver.find_element_by_xpath("//div[@class='js-with-permission-fields']/button[@type='submit'][@class='btn btn-primary first-in-line']").click()


        # Exit out of the window after the repo is created
        time.sleep(2) # Let the user actually see something!
        self.driver.quit()

"""
# Use the executable file in my desktop to start the chromedriver
service = Service('/home/abilashbodapati/Desktop/chromedriver')

# Start the chromedriver service
service.start()

# Target web-url initialized (Github login-page)
driver = webdriver.Remote(service.service_url)
driver.get('http://www.github.com/login')
# Maximize the window when the webpage is opened
driver.maximize_window()

'''
    This is the point 
    I am on the Github
    login page.
'''




# Passing username argument into login field
driver.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
# Passing password argument into password field
driver.find_elements_by_xpath("//input[@name='password']")[0].send_keys(password)
# Once the credentials are passed in, click on the submit button
driver.find_elements_by_xpath("//input[@name='commit']")[0].click()


'''
    This is the point 
    I am logged into 
    the github homepage.
'''

# Click on the "Create new repo button." 
driver.find_element_by_xpath("//a[@href='/new'][@class='btn btn-sm btn-primary text-white']").click()

# New Repository name and Description 
## We will use the values from the project creation script
repo_name = sys.argv[1]

# Passing the repo name provided by the input into the new Repo page
driver.find_element_by_xpath("//input[@name='repository[name]']").send_keys(repo_name)

# Slow down the transaction
time.sleep(2.5)

# Once the Repo details are filled out, click on the Create Repository button.
driver.find_element_by_xpath("//div[@class='js-with-permission-fields']/button[@type='submit'][@class='btn btn-primary first-in-line']").click()


# Exit out of the window after the repo is created
time.sleep(2) # Let the user actually see something!
driver.quit()
"""