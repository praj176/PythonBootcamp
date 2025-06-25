'''
A Python virtual environment is an isolated workspace where you can install and manage packages separately from the system-wide Python. 
It helps avoid version conflicts between projects. As sometimes project might need different versions of the same module which get updated.
'''
# First install the package in the terminal

# >> pip install virtualenv

python -m venv env_name #(name of the virtual environment)
# By default virtual environment is not activated, we need to activate the virtual environment before we want to use it.
env_name\Scripts\Activate.ps1
#Environment is activated

#Now we can install modules in this environment from scratch

# pip stands for “Pip Installs Packages” is the default package manager for Python 
#It is used to install and manage additional libraries and dependencies that aren’t included in the standard Python library.

pip install package_name

pip install --upgrade package_name #Upgrading a package

pip list # Lists all installed packages

pip uninstall package_name #uninstall

'''
Requirements.txt : It is a file which is for the users of your project 
The dependency of the project in a single file is called requirements.txt.
'''

pip freeze > requirements.txt # Creates the requirements.txt file which includes the list of all the packages with versions

deactivate  # To deactivate the virtual environment

# Let see how to install the requirements file in another environment
#1 Create a new virtual environment
python -m venv env_name2

# Activate the virtual environment
env_name2\Scripts\Activate.ps1
#Instead of installing each package individually, you can use the requirements.txt file—which lists all the necessary modules and their versions—to set up the new environment efficiently.

pip install -r requirements.txt
#scan all the packages inside my requirements.txt and install them one by one.

# Now you don't need to install the packages which were already installed in the previous virtual environment.
# The packages installed in this enviroment won't be installed in the global python environment.



