# Requests package helps Python talk to websites or APIs like asking for data or sending info.
#Install Request package
pip install requests #terminal

#python program
import requests

'''
GET Request : (You’re just asking for information not changing anything)
It asks a website or server for information and retrieves data from them!

How it works: The data you’re asking for is included in the URL.
Use cases:
 > Searching on Google
 > Loading a webpage
 > Fetching public data from an API
'''
r = requests.get("https://api.github.com")
# We will do the get request to get the information regarding the URL, 
#requests.get("URL") > retrieve data from the URL
print(r.text) # prints the data in the text data.
with open("github.txt", "w") as f:
  f.write(r.text)
# Content of the URL is written the github.txt file

'''
POST Requests : 
Purpose: Sends data to a server to create or update a resource.
How it works: Sends data in the request body, More secure for sensitive data like passwords.
>> It’s used when you want to create or update something.
Use cases:
 > Submitting a login form
 > Uploading a file
 > Sending form data to a server

'''

p = requests.post("https://library_example.com", data={'key': 'value'})


