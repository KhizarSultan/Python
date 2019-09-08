# Decorators 
# first class function and closure
from functools import wraps
import time
def square(a):
    return a**2


s = square # assign a function to s

print(s(7)) #49
print(s.__name__)
print(s)  # same
print(square) # same

# how to pass a function as a argument
#Assignment 
mylist = [1,2,3,4,5,6]
def my_map(func,l):
    return [func(item) for item in l]

print(my_map(square,mylist))
print(my_map(lambda key:key**3,mylist))

# A function return a function, called as first class function or closure function
def outer_func():
    def inner_func():
        print("Inner Function called")
    return inner_func  # return function

inn = outer_func() 
inn()







#Decodars intro 
# decorators are use to enhance the functonality of other functions 
# to add extra features in function without modified them
#  @ sytactic sugar

def decorator(any_function):
    @wraps(any_function)
    def wrapper_func(*args,**kwargs):
        '''This is a wrap function'''
        print(f"This is Owesome Function")
        return any_function(*args,**kwargs)
    return wrapper_func


@decorator  # shortcut , when func1 function will be called, decorator function will automatically called before the execution of func1
def func1():
    print(f"This is func1() ")

@decorator
def func2():
    print(f"This is func2()")
func1()
func2()

func1 = decorator(func1)

@decorator
def add(a,b):
    ''' this function will add two numbers '''
    return a+b

print(add(5,7))

print(add.__doc__)  # it will print wrapper function, not correct
# to solve this problem we import wrap from functools

print(add.__name__)


#Assignment of decorators

def add_decorator(fun):
    @wraps(fun)
    def wrapper_fun(*args):
        print("You are calling Wrapper function")
        return fun(*args)
    return wrapper_fun

@add_decorator
def myAdd(*args):
    '''This function will takes as many arguments as you want and will return their sum'''
    return sum(args)

print(myAdd.__doc__)
print(myAdd(1,2,3,4,5))


# 2nd assignment 
def cal_time(fun):
    @wraps(fun)
    def fun_wrapper(*args,**kwargs):
        print(f"Executing .... {fun.__name__}")
        t1 = time.time()
        ret_value = fun(*args,**kwargs)
        t2 = time.time()
        cal_time = t2-t1
        print(f"{fun.__name__} take {cal_time} in miliseconds")
        return ret_value
    return fun_wrapper    

# @cal_time
# def myfunc(l):
#     return [i**2 for i in l]

# mylist_2 = list(range(1,10000))

# print(myfunc(mylist_2))
        
#Assignment 3 about decorators

def only_int_allow(func):
    def wrapper_function(*args,**kwargs):
        if all([True if type(i)== int else False for i in args]): 
            return func(*args,**kwargs)
        print("Invalid Arguments")    
    return wrapper_function

@only_int_allow
def Sum_integer(*args):
    total = 0
    for i in args:
        total += i 
    return total

print(Sum_integer(1,2,3,4,5,6,[1,2,4,5,6])) # Error


#Decorator with arguments\
# are used for the any kinda data type
def only_data_types(data_type):
    def decorator(func):
        def wrapper_function(*args,**kwargs):
            if all([type(i)== data_type for i in args]): 
                return func(*args,**kwargs)
            else:
                print("Invalid Arguments")    
        return wrapper_function
    return decorator

@only_data_types(str)
def Sum_values(*args):
    total = ''
    for i in args:
        total += i 
    return total

print(Sum_values("khizar"," Sultan"," Islam",12,12)) #invalid
print(Sum_values(1,2,3,4,5,6)) 































