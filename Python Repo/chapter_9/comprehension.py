#List Comprehension
#simple way
squares = []
for i in range(0, 11):
      squares.append(i**2)
print(squares)
#comprehension way
#mylist = [append_Item loop]
square2 = [i**2 for i in range(0, 11)]
print(square2)

negative_list = [i for i in range(-1, -11, -1)]
negative_2 = [-i for i in range(1, 11)]
print(negative_list)
print(negative_2)
#simple way
names = ["Khizar", "Haider", "Habib"]
new_names = []
for name in names:
    new_names.append(name[0])
print(new_names)
#comprehension way
new_names_2 = [name for name in names]
print(new_names_2)
l = ['abc', 'def', 'ghi']
new_l = [i[::-1] for i in l]
print(new_l)

#if else using comprehension in List
#[Appenditem loop condition]
numbers = list(range(1, 11))
even_list = [i for i in numbers if i % 2 == 0]
odd_nums = [i for i in numbers if i % 2 is not 0]

print(even_list)
print(odd_nums)

#Simple way
mix_list = [1, 2, 3, "khizar", 1.23, 1.02, True, False]


def convert_to_str(l):
    str_list = []
    for i in l:
        if type(i) is not str:
            str_list.append(str(i))
    return str_list


print(convert_to_str(mix_list))
#comprehension way


def convert_to_str2(l):
    return [str(i) for i in l if type(i) is not str]
    
print(convert_to_str2(mix_list))
#list comprehension in if else
new_list = [i*2  if (i%2 == 0) else -i for i in numbers]
print(new_list)

#nested list comprehension
example = [[1,2,3],[1,2,3],[1,2,3]]
nested_list = [list(range(1,4)) for i in range(1,4)]
nested_list2 = [[i for i in range(1,4)] for j in range(1,4) ] 
print(nested_list2)

