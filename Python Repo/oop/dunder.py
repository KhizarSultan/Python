class phone: #base class
    def __init__(self,b,n,p):
        self.brand = b
        self.name = n
        self.price = p
    def full_name(self):
        return f"{self.brand} and {self.name} and {self.price}"    
    def make_call(self,phone):
        print(f"{phone} Calling ......")

    def __repr__(self):
        return f"{self.brand} and {self.name} and {self.price}"   
    def __len__(self):
        return self.price    
    def __add__(self,other):
        return self.price+other.price    


phone_1 = phone("OOPPO","A37",10000)

phone_2 = phone("OPPO","A57",5000)

print(phone_1) #it will call repr
print(len(phone_1)) #100000

# operator overrloading
print(phone_1+phone_2)

#polymorphism 
# many forms
