# Opens the file for writing. If the file exists, its contents will be overwritten(Entire file will be cleared and the content will be rewritten)
#If the file doesn't exist, a new file will be created

# write info in the text file

f = open("14_File_IO.py\\qew.txt", "w")
#Use relative path or the absolute path of the file and at last try to use double backward slashes (\\) instead of one to avoid Syntax errors for escape characters 
string = '''Jon doe is a good guy he is a guy who is good!'''
f.write(string)
f.close()
