# functions
#user define function

def Add_two(a,b):
    return a+b


# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# print(Add_two(a,b))

# a = input("Enter first name")
# b = input("Enter second name")
# print(Add_two(a,b))

#exercise 
def find_Last(a):
    return a[-1]

print(find_Last("khizar"))

def even_ooad(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"    

print(even_ooad(135613))

def is_even(num1):
    return num1%2 == 0

print(is_even(10))

def greater(a,b):
    if a>b:
        return a
    elif b>a:
        return b


#kiss keep it simple stupid

print(greater(greater(10,5),100))

#exercise 
def is_palindrome(name):
    lower_name = name.lower()
    R_name = lower_name[::-1]
    if R_name == name.lower():
        return True
    else :
        return False

print(is_palindrome("khizra")) #false
print(is_palindrome("Madam"))  #True

# exercise 2
for i in range(1,11):
    print(i,end = " ")
#default Paramaters
# Default Parameter would be Last in Parameters
# non-default arguments always follow default arguments
print("\n")
# def user_info(Fname,Lname,Age = 23):
#     print(f"Your First Name is {Fname} and Last Name is {Lname} and Your Age is {Age}")

def user_info(Fname = None,Lname = None,Age = None):
    print(f"Your First Name is {Fname} and Last Name is {Lname} and Your Age is {Age}")


# def user_info(Fname,Lname = None,Age):  # ERROR
#     print(f"Your First Name is {Fname} and Last Name is {Lname} and Your Age is {Age}")


user_info("khizar","Sultan")
user_info("khizar","Sultan",25)
user_info()


#Scope
x = 50
def func1():
    x = 10
    return x

print(func1()) #10
print(x) #50 

#How we can change the value of global variable in a function

x = 50
def func2():
    global x
    x = 10
    return x

print(func2()) #10
print(x) #10


