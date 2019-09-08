# oop is the style of code, use to manage the code and understandleable
# init method is just like the constructor in c++
# self is used for specific product but class instance is for all the product
import dunder as dund
class person:
    pi = 3.14  # Class variable
    def __init__(self,n,a,g):
        # instance variable
        self.name = n
        self._age = a # protected member
        self.__gpa = g # private member
        person.pi # access class variable

p1 = person("Khizar",20,3.20)
print(p1.name)


class laptop:
    count_instance = 0
    def __init__(self,b,m,p):  # just like setter constructor
        # instance variable
        laptop.count_instance += 1
        self.brand_name = b
        self.model_name = m
        self.price = p

    def full_name(self): # Instance mathod 
        return f"{self.brand_name} {self.model_name}"

    @classmethod # it is a class method and called by a class name
    def count_instances(cls): # cls represent an class
        obj = cls("HP","Zbopk",6000) # callling to a constructor
        return f"You have created {cls.count_instance} instances {obj}"
        
    @staticmethod # is just like instance method without passig self argument calling  by class name
    def hello():
        print("Hello World")    

l1 = laptop("HP","Zbook",50000)
l2 = laptop("HP","Zbook",50000)
l3 = laptop("HP","Zbook",50000)
print(l1.brand_name)
print(l1.full_name()) # same
print(laptop.full_name(l1)) # same
print(laptop.hello())
print(laptop.count_instances()) # 4 instance answer
print(l3.__dict__)


l = [1,2,3,4,5,6]
l.append(9) #same
list.append(l,10) #same
print(l) 


# Diff bw instance method and class method 
# diff between instance variable and class variable 

#Encaptulation
# define a method there where the data is present, not passing data in arguments
#jab tak encapsulation nhi hoti tab tak abstraction nhi ho sakti
# oop is public in python 
# __name__ dunder/magic mathods
#  __price name mangling, it will treat like a private
class phone:
    def __init__(self,br,mod,pr):
        self.brand = br
        self.modal = mod
        self.__price = max(pr,0) # for +ve price
        #self.description = f"{self.brand} and {self.modal} and {self.__price}" 
    # @property # this property will change the method into attribute
    # i.e this description function behave like a property/attribute
    def description(self):
        return f"{self.brand} and {self.modal} and {self.__price}"
    
    # @property # it is a getter
    def getprice(self):
        return self.__price

    # @getprice.setter # it is a setter
    def setprice(self,new_price):
        self.__price = new_price    
        print(f"Price set")
    
    #set_get = property(getprice,setprice)

    def full_name(self):
        print(f"{self.brand} and {self.modal}")    

mobile1 = phone("OPPO","A57",2200)
print(mobile1.brand)
print(mobile1.__dict__) #{'brand': 'OPPO', 'modal': 'A57', '_phone__price': 2200, 'description': 'OPPO and A57 and 2200'}
#print(mobile1.__price) # it will give an error because python change the __price to _phone__price, called name mangling

mobile1._phone__price = 15000
print(mobile1.__dict__) #after changing price still price does not change in description 
#{'description': 'OPPO and A57 and 2200'}
print(mobile1.description) # now update 

# Setter and getter
print(mobile1.setprice(2000))
print(mobile1.getprice())

# modeluling 
obj = dund.phone("apple","X",100)
print(obj.full_name())




