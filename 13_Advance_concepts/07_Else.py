try:
  a = 23/0

except Exception as e:
  print(e)

#Gets executed when there is no error in the try block
else:
  print("Code works fine")

'''
You won’t get the output from the else block because the try block raises an error, so the else block is skipped.
'''
