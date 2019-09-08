#List:
l = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print([[row[i] for row in l] for i in range(0,len(l)+1)])


numbers = [7,6,5,48,2,4,3]
print(numbers)
# print(numbers[:5])
# numbers[3:] = ["four","five","six","seven","eight","nine"]
print(numbers)

names = ["Asad","Haider","Habib","Khizar"]
print(names)
print(names[1:])

mixed = ["Asad",30,"haider",27,"Habib",24,"Khizar",20]
print(mixed)
print(mixed[::-1])

#How to add items in List
students = []
students.append("Khizar")
students.append("Ali")
students.append("Umair")
students.insert(0,"Asim")
students.insert(1,"Hamza")
print(students)

new_students = []
new_students.append("Hashir")
new_students.append("Bilal")
new_students.append("Sohail")

#concatenations

# All_Students = new_students + students 
# print(f"{All_Students}")

#Extend and Append
students.append(new_students) # Add list in list(Nested list)
print(students)

new_students.extend(students) # Add elements of list in List
print(new_students)

#how to Delete Items in List
students.pop() # delete last item
students.pop(1) #delete at specific index
print(students)
del new_students[1] 
print(new_students)
# how to delete the specific string from list
new_students.remove('Hamza')
print(new_students)

#how to check specific element is present in  list
if 'khizar'.lower() or 'khizar'.upper() or 'khizar'.title() in new_students:
    print("Khizar is Present")
else:
    print(f"Not Present")

#List Methods
# Append, Extend, insert
# del , pop, remove
# count, sort,reverse, clear,copy,sorted fucntion 

print(new_students.count('Khizar'))
print(students.sort())
popped_element = new_students.pop()
new_students.sort()
print(new_students)
# mixed.sort() #error
print(sorted(numbers)) #it will prints sortedly but not sort the list
print(numbers)

#List Comparison

# list1 == list2

#Split and Join ,,, Important

#Split converts string into List

user_info = "Khizar 24"   # 
print(user_info.split()) # ['khizar','24'] it will convert this string into list sepearetd from space
new_user = "Haider,23"
name,age = new_user.split(',') 
# print(new_user.split(','))  #convert into list
print(name,age)

#Join convert list into string
persons = ['Khizar','24']

print(','.join(persons))
print(' ! your Age is '.join(persons))

#mutable and immutable 
# Strings are Immutable and List are Mutable

mystring = "string"
new_string = mystring.title()  # it will not change in original string  

print(mystring) # string
print(new_string) # String

old_list = ['1','2','6','7']
old_list.pop() #it will change in origial list
print(old_list) # 1,2,6 so list are mutable(change in original variable)

#loops in LIST
for num in old_list:
    print(num,end=" ")
i = 0
while i< len(old_list):
    print(old_list[i])
    i+=1    
#Nested Lists 
matrix = [[1,2,3],[4,5,6],[7,8,9]] #2d list
print(matrix) #print list
#but what if we want to show the every element of our list then we use for loop
for sublist in matrix:
    for i in sublist:
        print(i,end=" ")
    print("\n")

print(matrix[1][2]) #6
print(matrix[::-1])
print(type(matrix))

#More about Lists
new_numbers= list(range(1,11))
print(new_numbers)
print(new_numbers.index(5)) # return the index of 5 value


#Pass list to a function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative    

print(negative_list(new_numbers))

def Square_list(l):
    Square = []
    for i in l:
        Square.append(i*i)
    return Square    
print(Square_list(new_numbers))


def Reverse_list(l):
    # l[::-1]
    #l.reverse()
    i = 1
    Reverse = []
    while i <= len(l):
      Reverse.append(l[-i])
      i += 1
    return(Reverse)

print(Reverse_list(new_numbers))

def rev_every_element(l):
    rev_list = []
    for i in l:
       rev_list.append(i[::-1])
    return rev_list
    
mylist = ['abc','def','ghi']
print(rev_every_element(mylist))

def even_add_separated(l):
    odd_list = []
    even_list = []
    mixed_list = []
    for i in l:
        if i%2 == 0:
            even_list.append(i)
        elif i%2 != 0:
            odd_list.append(i)
        else:
            pass
    mixed_list.append(odd_list)
    mixed_list.append(even_list)
    return mixed_list    

even_odd_list = [1,2,3,4,5,6,7,8,9]
print(even_add_separated(even_odd_list))

def inter_section(l1,l2):
    inter = []
    for i in l1:
        for j in l2:
            if i == j:
                inter.append(i)
            else:
                pass     
    return inter            

num1 = [1,2,3,4,5,6]
num2 = [1,2,3,5,8,9]
print(inter_section(num1,num2))

#min and max function
print(min(num1))
print(max(num2))

def greatest_diff(l):
    return max(l) - min(l)


print(greatest_diff(num2))    

def number_of_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
        else:
            pass
    return count    
nest_list = [[1,2,3],[2,4,5],[7,8,9],10,12]
print(number_of_list(nest_list))

