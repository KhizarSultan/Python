# *Operator *args
# *args mean unfinite numbers of arguments, it takes the nth number of arguments as an a one tuple
 
def totol_nums(*args):
    print(type(args)) # this *args is an a tuple which contains the nth number of arguments
    total = 0
    for nums in args:
        total += nums
    return total
print(totol_nums(1,2,3))
# print(totol_nums(1,2,3,4,5,6))

# *args with normal arguments4
def total_multiply(num,*args): # *args always come after simple arguments
    multiple = 1
    print(type(args))
    print(num)
    for i in args:
        multiple *= i

    return multiple
mylist = [2,3,4,5]
mytuple = (2,2,3)
print(total_multiply(2,3,1,4)) # 2 is simple argument while (3,1,4) is a tuple
print(total_multiply(5,mylist)) # it will treat mylist as an a single element
print(total_multiply(5,*mylist)) # Now it will unpack elements of list and conver
print(total_multiply(*mytuple)) # now 2 is a simple argument and (2,3) is a *args

# Assignment 1
def power_fun(num,*args):
    power_list = []
    if args:
        power_list = [i**num for i in args]
    else:
        print("you did not pass any args")    
    return power_list

numbers = tuple(range(1,100))    
# print(power_fun(3,*numbers))



# ** kwargs key word arguments
# it will takes nth arguments as an a Dictionary which have key:value

def func(**kwargs): #will take Arguments as an a Dictionary 
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key} : {value}")
d = {
    'name':"Khizar",
    'Age':24,
    'Semester':"6th"
}
func(firstName = "Khizar",LastName="Sultan") # key:value
func(**d) # ** will unpake the dictionary 

# def All_data_structure(a):
#     print(a)
# list_numbers =[1,2,3,4,5,6]
# dictionary_numbers = {"one":1,"two":2,"three":3}
# set_numbers = {1,2,3,4,5,6} 
# tuple_numbers = (1,2,3,4,5)
# All_data_structure(list_numbers)
# All_data_structure(dictionary_numbers)
# All_data_structure(set_numbers)
# All_data_structure(tuple_numbers)

# how to use all arguments
# PADK
# Parameters
# *agrs
# default parameters
# **kwargs
# PADK
def func2(name, *agrs, age=24,**kwargs): # 1 simple Arguments, 2 *agrs, 3 default arguments, 4 **kwargs 
    print(name)
    print(agrs)
    print(age)
    print(kwargs)

func2("Khizar" , 1,2,3,4,5,age=30,day_1="monday",day_2="sunday")

#Assignment 2

def Make_Title(l):
    return [i.title() for i in l]

list_2 = ["khizar","sultan","haider"]
#print(Make_Title(list_2))

print(list(map(lambda x:x[::-1],list_2)))




