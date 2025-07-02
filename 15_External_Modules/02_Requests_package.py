# Requests package helps Python talk to websites or APIs like asking for data or sending info.
#Install Request package
pip install requests #terminal

#python program
import requests

r = request.get("https://api.github.com")
# will do the get request to get the information regarding the URL, 
#requests.get("URL") > retrieve data from the URL
print(r.text) # prints the data in the text data.
with open("github.txt", "w") as f:
  f.write(r.text)
# Content of the URL is written the github.txt file


