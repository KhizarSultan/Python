#Tuples
# is a -data structure to store any kind of data but tuples are immutables
# they can not updated, can not change in original value
# no pop, no insert, no append , no remove
#tuples use when we know our data will not change and it is more faster than list
days = ('monday','tuesday','wednesday')

#methods:
# count(), len(), slicing, index()
print(days)
# days[0] = 'Monday' #Error
print(days[-1])
print(days.count('tuesday'))
print(days.index('wednesday'))

mixed = (1,2,3,4.0,"khizar")
for i in mixed:
    print(i)
#tuple with one element
one = (1) #it is integer not a tuple
two = (2,) # now it it tuple  
word = ("words") #it is a string not a tuple
word2= ("words",) #now it is a tuple
print(type(one)) #int   
print(type(two)) #tuple

print(type(word))
print(type(word2))


#tuple without parenthesis
fruits = 'Guava' ,'Melone','Apple'
print(type(fruits)) #tuple
print(fruits)

#Tuple Unpaking
guava,melon,apple = (fruits)
asad,haider,habib,khizar = 30,25,23,20
print(f"{guava} and {melon} and {apple}")
print(f"{asad} and {haider} and {habib} and {khizar}")

#List inside Tuples
names = ('khizar','Habib','Haider','Asad',[20,23,25,28],'Maryam')

# we can perfome all the fucntion and method of list to the list within in tuple 
names[4].pop()
print(names)
names[4].append(28)
print(names)

print(min(names[4]))
print(sum(names[4]))

def func1(num1,num2):
    sum = num1 + num2
    diff = num1 - num2
    mul  = num1 * num2
    if num2!=0:
        div = num1 / num2
    return sum,diff,mul,div # it will return a tuple that contains the answers like this (sum,diff,mul,div)

sum,diff,mul,div = (func1(10,10))
print(f"The sum is {sum} and Difference is {diff} and Multiplication is {mul} and the Division is {div}")


# we can change the tuple into list
numbers = tuple(range(1,11)) # tuple
print(numbers)
numbers_list = list(numbers) #now this is converted into list
print(numbers_list)
string_numbers = str(numbers_list) #now this is converted into string
print(string_numbers)






