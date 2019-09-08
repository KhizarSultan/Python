#if statement 
name = "Khizar"
if name == "khizar" or name == "Khizar":
    print(f"you are khizar")
    print(f"you are above 23")
elif name == "khizra" or name == "khizra":
    print(f"you are khizra")
else:
    print("Neither khizar nor khizra")

#pass statement 
age= 24
if age == 23:
    print(f"you are 23 years old")
else:
    pass    
#exercise
# guess = 100
# num = int(input("Please Guess the number"))
# if num == 100:
#     print(f"you are winner")
# elif num != 100:
#     if num <= 100:
#         print("too low")
#     elif num >=100:
#         print("too high")
# else:
#     pass


#  'in'  keyword to find a special character

if 'i' in name:
    print("i is Present")
else:
    print("not present")

if name:
    print("String is not empty")
else:
    print("string is empty")

# loops
# exercise 1
# i = 1
# while i<10:
#      print("Hello World")
#      i+=1
# user_num = int(input("Please Enter Number"))
# j = 1
# while j<=user_num:
#     print(f"Hello World {j}")
#     j+=1 

# #exercise 2
# total = 0
# i = 0
# user_num = input("please enter number: ")
# if user_num == "":
#     print("Please Enter number")
# else:
#     while i < len(user_num):
#         total = total + int(user_num[i])
#         i += 1
#     print(total)    

#exercise 3

# name = input("Please enter your name")
# i = 0
# while i < len(name):
#     print(f"{name[i]} : \t {name.count(name[i])}")
#     i+=1

# for loop with range function

# for i in range(10): # range(10) mean 0 to 9
#     print(f"hello {name}")

for i in range(1,11): # range(1,11) mean 1 to 10
    print(f"hello {name}")

for i in range(0,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in "Khizar Sultan":
    print(i)

#DRY don't repeat yourself. 



   

