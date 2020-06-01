'''
    File Name: CreateProject.py
    Author: Abilash Bodapati
    Version: 20200531
    Description
'''

# Import all the libraries I need
import os
import sys
from pathlib import Path
import CreateGitRepo



# Function to create the project
def createProject(argv):
    try:
        # Change the current working Directory
        os.chdir("/home/abilashbodapati/Desktop/Projects/")
        print("Directory changed to /Desktop/Projects")
    except OSError:
        print("Can't change the Current Working Directory")     


    try:
        # Create a new Directory
        os.mkdir(argv[0] + "/")
        print("Directory Created in /Desktop/Projects")
    except OSError:
        print("Directory already exists")

    try:
        # Change the current working Directory
        os.chdir("/home/abilashbodapati/Desktop/Projects/" + argv[0] +"/")
        print("Directory changed to " + argv[0] + " Folder")
    except OSError:
        print("Can't change the Current Working Directory")    

    # Create a Read me File
    os.system("echo \"# %s\" >> README.md" %(argv[0]))


# Main Function
if __name__ == "__main__":
    createProject(sys.argv[1:])