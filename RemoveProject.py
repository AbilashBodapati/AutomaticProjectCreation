'''
    File Name: RemoveProject.py
    Author: Abilash Bodapati
    Version: 20200616
    Description: 
        This is a Python script that removes the projects by 
        going to the directory and removing all the files and
        the directory itself, along with the repository in the
        github repo.
'''

# Import all the libraries I need
import os
import sys
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from RemoveGitRepo import RemoveGitRepo



# A class to hold all the functions for 3 main steps
class RemoveProject:

    # Constructor for this class that store the command line arguments
    def __init__(self, argv):
        """
            arg[0] => RootFolder in the Project folder
            arg[1] => Username
            arg[2] => Password        
        """
        self.parent_folder_name = argv[0]
        self.username = argv[1]
        self.password = argv[2]


    # Function to force Remove Project Folder
    def removeFiles(self):
        # Remove all File from the project folder
        print("")
        print("==============DELETING THE PROJECT FROM YOUR SYSTEM==============", end='\n')
        time.sleep(1.75)
        #####os.chdir("/home/abilashbodapati/Desktop/Projects")
        #####os.system("rm -rf %s" %(self.parent_folder_name))
        print("")
        print("==============DELETED THE PROJECT FROM YOUR SYSTEM==============", end='\n')
        time.sleep(1.75)

    # Function to Execute all the Git commands
    def executeGit(self):

        # Run a Separate python script to Remove git repo on github
        #os.system("python3 ../PrivateFiles/CreateGitRepo.py %s" %(self.parent_folder_name))
        print("")
        print("==============DELETING THE PROJECT FROM YOUR GITHUB==============", end='\n')
        time.sleep(1.75)
        removeGit = RemoveGitRepo()
        removeGit.construct(self.parent_folder_name, self.username, self.password)
        removeGit.startChromeService()
        removeGit.accessGithub()
        removeGit.removeRepo(self.parent_folder_name)
        print("")
        time.sleep(1.75)
        print("==============DELETED THE PROJECT FROM YOUR GITHUB==============", end='\n\n')
        time.sleep(1.75)
        print("In the meanwhile, I hope you get new and innvoative ideas for a new project.")
        time.sleep(1.5)



# Main Function
if __name__ == "__main__":
    #createProject(sys.argv[1:])
    project = RemoveProject(sys.argv[1:])
    
    project.removeFiles()
    project.executeGit()
