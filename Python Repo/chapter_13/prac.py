#Enumration 
# we use Enumeration function with for loop to get the postion

names = ["khizar","Ali","Umair","Fahad"]
for name in names:
    print(name)

for pos,name in enumerate(names):  #now pos have the index of each value in a list
    print(f"{pos} --- >{name}")    

def Find_Index(l,s):
    for pos,name in enumerate(l):
        if s == name:
            return pos
    return -1
print(Find_Index(names,"fahad"))
# find the length of each element in a list
mylist = ["khizar","habib","asad","cake"]
length = list(map(len,mylist))    # map function is used if we call a functions thousand time, instead of for loop, we use map function
# map(function_name,dataStructure)
print(type(length))
for i in length:
    print(i)


#Filter Function is use to filter any data structure just like map
def even(a):
    return a%2==0

mix_list = list(range(1,11))
even_list = list(filter(lambda l: l%2==0 ,mix_list))
odd_list = list(filter(lambda a: a%2!=0,mix_list))

# even_list_2 = list(filter(even,mix_list)
# 
# print(even_list_2)
print(even_list)
print(odd_list)
len_list = list(map(lambda l:len(l), mylist))
print(len_list)


# Zip function is used to pack and unpack of any data structure
# Zip Function takes two data structure and make them tuple (16F8153,khizar),(16F8196,Ali)
users_id = ["16F8153","16F8196","16F8256"]
users_names = ["Khizar","Ali","Umair"]
print(dict(zip(users_id,users_names)))  # {"16F8153":"Khizar","16F8196,"Ali"}

mixed_list = [(1,2,9),(3,4,10),(5,6,11),(7,8,12)]
odd,even,after = zip(*mixed_list) # it will unpake the list and make their tuple e.g (1,3,5,7) and (2,4,6,8)
print(odd)
print(even)
print(after)
max_list = []
for pair in zip(odd,even): #it will make their tuple(1,2),(3,4) .... 
    max_list.append(max(pair))

print(max_list)

# Assignment
def average(*args):
    ave = []
    for pair in zip(*args):  # return tuple 
        ave.append(sum(pair)/len(pair))
    return ave

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list4 = [10,11,12]
print(average(list1,list2,list3,list4))

avrage_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(avrage_finder(list1,list2,list3,list4))


#Any and all Function

# All--> if all values in list are True than return true
# any--> if any value in list is true than return true

print(all([True,True,True])) 
print(all([i%2==0 for i in range(1,11)]))
print(any([True,False,False]))

# advance min and max
names_list = ["KhizarSultan","Ali","Umair"] # find the maximum lenght of name in this list
# print(max(names_list)) # umair , its wrong

print(max(names_list,key = lambda item:len(item)))   # key = function
print(min(names_list,key = lambda name:len(name))) 


#Assignment , Find the name of max score
students = [
    {
    'Name':"KhizarSultan",
    'Age':20,
    'Score':60
    },
    {
    'Name':"Ali",
    'Age':23,
    'Score':50
    },
    {
    'Name':"Umair",
    'Age':25,
    'Score':20,
    }
]
print(sorted(students, key=lambda d: d['Score'],reverse = True))
print(max(students,key = lambda MyDict: MyDict['Score'])['Name']) # find the maximum score
print(max(students,key= lambda item:item.get('Age'))['Name'])  # Max Age

# Doc String is ued to tell about the code 

def Add(a,b):
    ''' It will print The sum of Two numbers '''
    return a+b
print(Add.__doc__)
print(len.__doc__)
print(help(sum))
print(sum.__doc__)































     













