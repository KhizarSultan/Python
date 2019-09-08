# Generators are iterators
# what is iterator

l = [1,2,3,4,5] #iterable
i = iter(l)     #it will change the iterable(list) in iterator 
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# we can next function use in iterable
for num in map(lambda a:a**2,l):
    print(num)

def even_generator(n):
    for i in range(1,n+1):
        if i%2 == 0:
            yield(i) # it is just like the return fucntion but it does not save in memoery
        else:
            pass
for num in even_generator(20):
    print(num)
# generator comprehension
square = (num**2 for num in range(0,21,2))
print(square)
for num in square:
    print(num)
