#Opens the file for appending. Data will be added to the end of the file. 
#If the file doesn't exist new file will be created. 
#Append to an existing file called test.txt file
# add more info regarding random info

f = open("14_File_IO.py\\qew.txt", "a")
#Use relative path or the absolute path of the file and at last try to use double backward slashes (\\) instead of one to avoid Syntax errors for escape characters 

string = '''Jon doe is a engineer. working in a good company as data science expert. he lives in Johanesburg'''
f.write(string)
f.close()
