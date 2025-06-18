# Opens the file for writing. If the file exists, its contents will be overwritten 
#(If the file doesn't exist, a new file will be created)

# write info in the text file

f = open("14_File_IO.py\qew.txt", "w")

string = '''Jon doe is a good guy he is a guy who is good!'''
f.write(string)
f.close()
