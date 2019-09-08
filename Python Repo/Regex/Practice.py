import re

str = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", str)

print(x)


str = "That will be 59 dollars"

#Find all digit characters
x = re.findall("\d", str)
print(x)


str = "hello world"

#Search for a sequence that starts with "he", followed by two (any) characters, and and with "o":
x = re.findall("he..o", str)
print(x)


str = "hello world"

#Check if the string starts with 'hello':
x = re.findall("^hello", str)
if (x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
str = "hello world"

#Check if the string ends with 'world':
x = re.findall("world$", str)
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")

  str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")



str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")  


str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
