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

'''Requirements.txt'''

pip freeze # list downs all the packages with versions

