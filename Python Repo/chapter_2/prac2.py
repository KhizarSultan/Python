#strings
name = "Khizar"
name,age = "KhizarSultan", 23

print(name[0])
print(name[-1])
#slicing
# print(name[startIndex:EndIndex+1])
# start_Argument:Stop_Argument,step_argument

print(name[0:3]) #khi
print(name[6:]) #sultan
print(name[0:-6]) #khizar
print(name[-4:])
print(name[:-6])

print(name[0:-6:2])
print(name[::-1])

#user input
# age = int(input("Please Enter Your Age: ")) #its a string
# print(age)

# name,age = input("Enter name and age: ").split(",")
print(len(name))

print(name.lower())
print(name.upper())
print(name.title())
print(name.replace("i","I",1)) #it will not change the video

print(name.find("a",5))
pos_1 = name.find("a")
pos_2 = name.find("a",pos_1+1)


print(pos_2)

print(name.center(len(name)+4,"*")) #4 is the number of start

#string are immutable 
My_name = "Khizar"
# My_name[2] = "S"  #Error
print(My_name) 

fida = "        FIDA HUSSAIN       "
print(fida)
print(fida.strip())
print(fida.replace(" ",""))

#string Formatting

print(f"My name is :{name} and My age is :{age+5}")

mylist = [1,2,3,4,5,6,7]
for i in mylist:
    print(i)
    

# print(name[0:-6:2])