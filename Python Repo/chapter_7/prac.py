#Dictionaries
#Unordered Collection of data in key:value
#There is no index in the Dictionary

user = {'name' : "khizar" , 'age' : 20}
print(user)
print(type(user))
#Second method to create dictionary
user1 = dict(name = "Khizar",age = 21, Semester = 6)
print(user1)
#how to access data from dictionary

print(user['name'])
print(user1['Semester'])
print(user['age'])

#Any thing can be store in Dictionary

user_info = {
    'name': 'Khizar',
    'age':21,
    'fav_movies':['DDLJ','Qismat','YJHD'],
    'fav_tunes':['Nokia','Balance','Birds','Awakening']
}
# print(user_info)
print(f"My Favourites Movies are {user_info['fav_movies']}")

#Nested Dictionaries
users = {
    'user1' : {
        'name':'khizar',
        'age':22,
        'semester':6
    },
    'user2': {
        'name':'Haider',
        'age':26,
        'semester':8
    },
}
print(users['user1'])

#how to add data into empty dictionary

user_info2 = {}
user_info2['name'] = "Khizar"
user_info2['age'] = 20
user_info2['semester'] = 6
user_info2['university'] = "Fast National University of computer and Emerging Sciences"
print(user_info2)

# In keyword and Looping in Dictionary
#Check if the key present in Dictionary or not

if 'name' in user_info2:
    print('Present')
else:
    print("Not Present")    

#Check if the value is Present in Dictionary or not

if 'Khizar' in user_info2.values():
    print('Present')
else:
    print("Not Present")    
 
#Loops in Dictionary
for i in user_info:
    print(i) # Will Print all the keys 

for i in user_info.values():
    print(i) # Will Print all the values
#Same
for i in user_info:
    print(user_info[i]) # Will Print all the values


print(type(user_info.values())) #Dic_values
print(type(user_info.keys())) #Dic_keys

#item Method
user_items = user_info.items() #Return a tuple contains a (key:value)
print(user_items) #([('name', 'Khizar'), ('age', 21), ('fav_movies', ['DDLJ', 'Qismat', 'YJHD']), ('fav_tunes', ['Nokia', 'Balance', 'Birds', 'Awakening'])])
print(type(user_items))

#Why item Method is important
for key,value in user_info.items():
    print(f"Key is {key} and Value is {value}") 

#How to Add data
user_info['fav_actors'] = ['Fawad Khan','Shahid Kapoor','SRK']
print(user_info)

#How to Delete Data
#pop will return the key and value
pooped_item = user_info.pop('age')
print(pooped_item)
print(user_info)

#Pop and PopItem method
#popitem delere random key value
#pop item return a tuple which contains the key and value

pop_item = user_info2.popitem()
print(pop_item)
print(user_info2)


# Method in Dictionary
#Update mathod add the dictionary in a dictionary

user_info.update(user_info2)
print(f"The Update method is {user_info}")

#Fromkeys method to create Dictionary
d = dict.fromkeys(['name','age','class'],"Unknown")
d2 = dict.fromkeys(('Roll_number','Name','Semester','GPA'),"Unknown")
print(f"{d} and {d2}")

#Get Method
#Get method is use to get the value from dictionary without knowning the key
print(d.get('name')) #return Unknow
print(d.get('Nameshfgh')) #return none

if d.get('name'):
    print("Present")
else:
    print("Not Present")

#Clear method to erase all the data from dictionary
d.clear()
print(d)
d['name'] = "Khizar"
d['age'] = 19
d['age'] = 20 #same keys will over ride


print(d)
#Copy method is use to copy the whole dictionary
d2 = d.copy()
print(d2)

print(d2 is d) # is check whether d and d2 are the same dictionary in memory or not

#More About Dictionaries

print(d2.get("names")) #None 
print(d2.get("names","Not found!")) #Not found

def cube_finder(n):
    cubes = {}
    for i in range(0,n+1,1):
        cubes[i] =i**3
    return cubes     
print(cube_finder(10))

# def Stor_Data_in_Dictionary()

# name,age,movies,songs = input("Please Enter Name,Age,Movies,Songs").split(",")
New_User = {}

name = input("Please Enter Name: ")
age  = input("Please Enter Age: ")
movies = input("Please Enter movies separated by , ").split(",")
songs = input("Please Enter Songs separated by , ").split(",")

New_User['Name'] = name
New_User['Age'] = age
New_User['Movies'] = movies
New_User['Songs'] = songs

for key,value in New_User.items():
    print(f"{key}:{value}")


































