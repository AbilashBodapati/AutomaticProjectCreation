# Create Project 
## Shell script that controls the execution of all files for Creating
First step is to open the terminal on the desktop.
Then change directory into Projects folder.
	
	cd Desktop/Projects/

Make a New Directory/Folder
	mkdir "FOLDER NAME" (Input the name of the folder name)


Change directory into the new directory
	cd "Desktop/Projects/FOLDER NAME/"

Create a README file
	echo "# 'FOLDER NAME'" >> README.md

Create a new file(s)
	touch ('file name'.py or 'file name'.java or 'file name'.ipynb)
	(Account for String Manipulation)
	(Files created have templates copied from my private folder into the project file)


Perform git actions

	git init
	git add *
	git commit -m "first commit"

	(Call the script to run the githubrepo creation)

	git remote add origin https://github.com/AbilashBodapati/FOLDERNAME.git
	git push origin master

By Now both the projects on system and github repo should be Created.


# Remove Project
## Shell script that controls the execution of all files for Removing
First step is to open the terminal on the desktop.
Then change directory into Projects folder.
	cd Desktop/Projects/

Force remove Directory/Folder and its contents
	rm -rf "FOLDER NAME" (Input the name of the folder name)

Perform git actions
	(Call the script to run the githubrepo remove)

By Now both the projects on system and github repo should be Deleted.
