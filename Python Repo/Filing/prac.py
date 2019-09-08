
f = open("c:/Users/Khizer/Desktop/cake.txt",'r')

# #cursor position
# print(f.tell())
# print(f.read())
# print(f.tell())
# #change the cursor position
# print(f.seek(20))
# print(f.read())

# print(f.seek(0))
# lines = f.readlines()[:2]
# for line in lines:
#     print(line,end=',')
# print(len(lines)) #3    
# print(f.seek(0))
# print(f.readline()) 
# print(f.readline()) 
# print(f.readline()) 
# print(f.closed)#False, is closed file or not?
# f.close()
# print(f.closed) # True

# print(f.name) # filename


# Read file with block
with open("c:/Users/Khizer/Desktop/cake.txt",'r') as f:
    data = f.read()
    print(data)
    
print(f.closed)# true










