#Inheritance
class phone: #base class
    def __init__(self,b,n,p):
        self.brand = b
        self.name = n
        self.price = p
    def full_name(self):
        return f"{self.brand} and {self.name} and {self.price}"    
    def make_call(self,phone):
        print(f"{phone} Calling ......")

class smartphone(phone): # class drive(baseclass)
    def __init__(self,b,n,p,ram,camera):
        super().__init__(b,n,p) # it will set the b,n,p
        self.ram = ram
        self.camera = camera
    def full_name(self): # method overriding
        return f"{self.brand} and {self.price} and {self.ram} and {self.camera}"    

# method resolution order
phone_obj = phone("OOPPO","A37",10000)
smtobj = smartphone("OOPO","A57",15000,"16GB","1.6M")
print(smtobj.full_name())

print(help(smartphone))

# isinstance and issubclass function
print(isinstance(smtobj,smartphone)) # true
print(isinstance(smtobj,phone)) # also true, because phone class is inherited into smartphone class
print(isinstance(phone_obj,smartphone))# false 

print(issubclass(smartphone,phone)) #true, is smartphone is inherited from phone
print(issubclass(phone,smartphone)) #false 

# Abstract class in python
# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 

class Polygon(ABC): 

	# abstract method 
	def noofsides(self): 
		pass

class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 

class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 

class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 

class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 

# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 






