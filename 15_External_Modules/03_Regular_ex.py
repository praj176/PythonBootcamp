'''
Regular expressions (or regex) in Python are like powerful search tools for text—they help you find, match, or manipulate patterns in strings.
You use it to:
 > Check if a string contains a pattern
 > Extract specific parts of a string
 > Replace or split text based on patterns
 
 '''
import re #Built in module

text = 'The quick brown fox jumps over the lazy dog.'
#Search for a pattern
match = re.search("brown",text)
if match:
    print("Match found")
    print("Start index: ",match.start()) # Returns the first occurrence in the sequence
    print("End index: ",match.end())

#To find all occurrence of a instance :
matches = re.findall("the", text, re.IGNORECASE) # Does the case INsensistive search
print("Matches: ",matches)
