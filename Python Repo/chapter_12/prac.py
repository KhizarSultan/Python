#Lambda Expression
# Anonymmous functions

#simple function
def add(*args):
    total = 0
    for i in args:
        total += i        
    return total
print(add(1,2,3,4))

#lambda function
# lambda no.of arguments: return
power =  lambda *args:[i**2 for i in args]
print(power(*list(range(1,11))))

even = lambda *args: [i for i in args if i%2==0]
print(even(*tuple(range(1,11))))

func = lambda num: True if num % 2 == 0 else False
print(func(10))

last_return  = lambda a: a[-1]
print(last_return("khizar"))

# less = lambda num : True if len(num) > 5 else False
# print(less(9))

