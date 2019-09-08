#Dictionary Comprehension and Set Comprehension
#dictionary have key:value pair

#Normal way
squares = {"name":"khizar","age":19}
print(squares)

#comprehension way
squares = {num:num**2 for num in range(1,11,1)}
squares_2 = {f"The Square of {num} is ":num**2 for num in range(1,11,1)}
print(squares_2)
for key,value in squares_2.items():
    print(f"{key} : {value}")
name = "KhizarKhizarSultan"
word_count = {char:name.count(char) for char in name}
print(word_count)

odd_dict = {i:("even" if i%2==0 else "Odd") for i in range(1,11)}
print(odd_dict)

#set Comprehension
my_set = {i**2 for i in range(1,11)}
print(my_set)






