'''
    File Name: CreateProject.py
    Author: Abilash Bodapati
    Version: 20200531
    Description
'''

# Import all the libraries I need
import os
import sys
import time
from pathlib import Path



# Function to create the project
def createProject(argv):
    try:
        # Change the current working Directory
        os.chdir("/home/abilashbodapati/Desktop/Projects/")
        print("Directory changed to /Desktop/Projects")
    except OSError:
        print("Can't change the Current Working Directory")
        sys.exit()     


    try:
        # Create a new Directory
        os.mkdir(argv[0] + "/")
        print("Directory Created in /Desktop/Projects")
    except OSError:
        print("Directory already exists")
        sys.exit()

    try:
        # Change the current working Directory
        #projectPath = "/home/abilashbodapati/Desktop/Projects/%s/ " %(argv[0])
        os.chdir("/home/abilashbodapati/Desktop/Projects/" +argv[0] + "/")
        print("Directory changed to " + argv[0] + " Folder")
    except OSError:
        print("Can't change the Current Working Directory")
        sys.exit()

    # Create a Read me File
    os.system("echo \"# %s\" >> README.md" %(argv[0]))

    # Ask user what file to create
    filename = argv[1]
    filetype = argv[2]
    
    # Creates the File in the project folder
    try:
        os.system("touch %s.%s" %(filename, filetype))
        if filetype == 'java' or filetype == 'Java':
            print('Created a Java file')
        elif filetype == 'py' or filetype == 'Py':
            print('Created a Python file')
    except OSError:
        print("File Already Exists")
        sys.exit()

    # Perform the Git actions
    os.system("git init")
    os.system("git add *")
    os.system("git commit -m \"First Commit.\"")

    # Run a Separate python script to create a git repo on github
    os.system("python3 ../PrivateFiles/CreateGitRepo.py %s" %(argv[0]))

    # Set remote url to origin
    os.system("git remote set-url origin https://AbilashBodapati@github.com/AbilashBodapati/%s.git" %(argv[0]))

    # Push the commit to the repo
    os.system("git push -u origin master")

    # Type out the password
    os.system(argv[3])

    # Open the project tree in vscode
    os.system("code .")



# Main Function
if __name__ == "__main__":
    createProject(sys.argv[1:])