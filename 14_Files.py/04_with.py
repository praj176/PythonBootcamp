# >> Normal method to read a file
# f = open("14_File_IO.py\\qew.txt", "r")
# content = f.read()
# print(content)
# f.close()

#Better approach
with open("14_File_IO.py//openme.txt","r") as f:
    content = f.read()
    print(content)
    
# No need to write f.close() Because file is automatically closed using the with.

