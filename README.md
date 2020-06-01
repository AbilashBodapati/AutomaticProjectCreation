# Create Project

First step is to open the terminal on the desktop.
Then change directory into Projects folder.
	cd Desktop/Projects/

Make a New Directory/Folder
	mkdir "FOLDER NAME" (Input the name of the folder name)


Change directory into the new directory
	cd "Desktop/Projects/FOLDER NAME/"

Create a README file
	echo "# 'FOLDER NAME'" >> README.md

Create a new file
	touch ('file name'.py or 'file name'.java)
	(Account for String Manipulation)


Perform git actions

	git init
	git add *
	git commit -m "first commit"

	(Call the script to run the githubrepo creation)

	git remote add origin https://github.com/AbilashBodapati/FOLDERNAME.git
	git push origin master


Final terminal command will be:
	python3 "ScriptName" "FOLDER NAME" ("file name.py" or "file name.java")

Global Environment variables
git config --global credential.helper store
	USERNAME = ""
	PASSWORD = "" 
