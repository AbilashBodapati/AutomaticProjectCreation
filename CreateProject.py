'''
    File Name: CreateProject.py
    Author: Abilash Bodapati
    Version: 20200531
    Description: 
        This is a Python script that creates the projects by 
        creating a new directory, adds all the necessary files needed,
        perform git operations for a First commit to the github repo,
        and finally open the vscode under the folder to start working.
'''

# Import all the libraries I need
import os
import sys
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from CreateGitRepo import CreateGitRepo



# A class to hold all the functions for 3 main steps
class NewProject:

    # Constructor for this class that store the command line arguments
    def __init__(self, argv):
        """
            arg[0] => RootFolder in the Project folder
            arg[1] => Filename of the Project
            arg[2] => File Extension (py or ipynb or java)
            arg[3] => Username
            arg[4] => Password        
        """
        self.parent_folder_name = argv[0]
        self.file_name = argv[1]
        self.file_ext = argv[2]
        self.username = argv[3]
        self.password = argv[4]

    # Function to create a new Directory to creat a new project
    def createNewDirectory(self):
        try:
            # Change the current working Directory
            os.chdir("/home/abilashbodapati/Desktop/Projects/")
            print("")
            print("==============Directory Changed to /Desktop/Projects==============", end='\n')
            time.sleep(1.75)
        except OSError:
            print("Can't change the Current Working Directory")
            sys.exit()     


        try:
            # Create a new Directory
            os.mkdir(self.parent_folder_name + "/")
            print("")
            print("==============Directory Created in /Desktop/Projects==============", end='\n')
            time.sleep(1.75)
        except OSError:
            print("Directory already exists")
            sys.exit()

        try:
            # Change the current working Directory
            #projectPath = "/home/abilashbodapati/Desktop/Projects/%s/ " %(argv[0])
            os.chdir("/home/abilashbodapati/Desktop/Projects/" + self.parent_folder_name + "/")
            print("")
            print("==============Directory Changed to " + self.parent_folder_name + " Folder==============", end='\n')
            time.sleep(1.75)
        except OSError:
            print("Can't change the Current Working Directory")
            sys.exit()


    # Function to create Files => README.md and file name
    def createFiles(self):
        # Create a Read me File
        os.system("echo \"# %s\" >> README.md" %(self.parent_folder_name))
        print("")
        print("==============README CREATED==============", end='\n')
        time.sleep(1.75)
        
        # Creates the File in the project folder
        try:
            #os.system("touch %s.%s" %(self.file_name, self.file_ext))
            # Java project
            if self.file_ext == 'java' or self.file_ext == 'Java':
                os.system("cp ../PrivateFiles/Template.java %s.java" %(self.file_name))
                os.system("cp ../PrivateFiles/TemplateClass.java %sClass.java" %(self.file_name))
                print("")
                print('==============CREATED A JAVA PROJECT==============', end='\n')
                time.sleep(1.75)
            # Python Project (Script or DataScience Notebook)
            elif self.file_ext == 'py' or self.file_ext == 'Py':
                os.system("touch %s.%s" %(self.file_name, self.file_ext))
                print("")
                print('==============CREATED A PYTHON PROJECT==============', end='\n')
                time.sleep(1.75)

            elif self.file_ext == 'ipynb':
                os.system("cp ../PrivateFiles/datascienceTemplate.ipynb %s.ipynb" %(self.file_name))
                # Create a new Directory
                os.mkdir("Datasets")
                print("")
                print("==============Datasets FOLDER CREATED==============", end='\n')
                time.sleep(1.75)
                ## TO-DO -- Be able to go on kaggle and download the datasets.
                print("")
                print('==============CREATED A DATASCIENCE PROJECT==============', end='\n')
                time.sleep(1.75)

        except OSError:
            print("File Already Exists")
            sys.exit()

    # Function to Execute all the Git commands
    def executeGit(self):
        # Perform the Git actions
        os.system("git init")
        os.system("git add *")
        os.system("git commit -m \"First Commit.\"")
        print("")
        print("==============PROJECT IS NOW A GIT PROJECT==============", end='\n')
        time.sleep(1.75)

        # Run a Separate python script to create a git repo on github
        #os.system("python3 ../PrivateFiles/CreateGitRepo.py %s" %(self.parent_folder_name))
        print("")
        print("==============CREATING A GIT REPOSITORY==============", end='\n')
        time.sleep(1.75)
        createRepo = CreateGitRepo()
        createRepo.construct(self.parent_folder_name, self.username, self.password)
        createRepo.startChromeService()
        createRepo.accessGithub()
        createRepo.createRepo()
        print("")
        print("==============CREATED A GIT REPOSITORY==============", end='\n')
        time.sleep(1.75)


        # Add remote url to origin
        github_path = "https://AbilashBodapati@github.com/AbilashBodapati"
        os.system("git remote add origin %s/%s.git" %(github_path,self.parent_folder_name))

        # Push the commit to the repo
        # Credentials stored
        os.system("git push -u origin master")
        print("")
        print("==============PUSHED CODE INTO REPO==============", end='\n')
        time.sleep(1.75)
        print("Your project has been created successfully. Good luck and have fun with your project!")
        time.sleep(1.5)

    # Function to open up the code editor
    def openVSCode(self):
        # Open the project tree in vscode
        print("")
        print("==============OPENING VS CODE==============", end='\n')
        time.sleep(2)
        os.system("code .")

"""

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

    # Add remote url to origin
    os.system("git remote add origin https://AbilashBodapati@github.com/AbilashBodapati/%s.git" %(argv[0]))

    # Push the commit to the repo
    # Credentials stored
    os.system("git push -u origin master")

    # Open the project tree in vscode
    os.system("code .")
"""


# Main Function
if __name__ == "__main__":
    #createProject(sys.argv[1:])
    project = NewProject(sys.argv[1:])
    
    project.createNewDirectory()
    project.createFiles()
    project.executeGit()

    project.openVSCode()