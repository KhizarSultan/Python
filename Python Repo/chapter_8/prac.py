#intro to Sets, mutable
#unordered collection of unique items(not repeated)
#it is just like dictionary but it is without key
#there is no indexing and positioning , it is unordered
#it is use ful to remove duplication in any datastructure
#can not store list,tuple in set

def remove_duplicate(l):
    s = set(l) #will remove all duplictes
    l2 = list(s) #will again convert into list
    return l2


mylist = [1,2,3,1,4,1,2,4,5,2,4,5,5,4,4,5,6,4,4,5,5,5]
print(remove_duplicate(mylist))

myset = {5,4,6,1.02,"Khizar",-63251}

#Set methods
myset.add(1)
myset.add(2)
myset.add(7)
myset.discard(7) #will delete
myset.discard(99) #can not delete becasue set have no 99 element
set3 = myset.copy()
print(myset.clear()) #will clear
print(set3)


#looping in sets

for i in set3:
    print(i,end = " ")


#Set Math
#Union and Intersection

s1= {1,2,3,4,5}
s2 = {4,5,6,7,8,9}
print("\n")
def find_union_and_intersection(s1,s2):
    union_set = s1 | s2
    intersection_set = s1&s2
    return union_set,intersection_set
print(find_union_and_intersection(s1,s2))



