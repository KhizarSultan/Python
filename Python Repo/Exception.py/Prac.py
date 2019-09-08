# Debugging errros and build in errors
while True:
    try:
        age = int(input("Please Enter Age"))
    except:
        print("Enter number ...")   
    else: # else run when exception not occur 
        #raise TypeError("This is typeError")
        print(f"Your age is {age}")
        break
    finally: # this block always run, even exception occur or not
        print("Finally calling...")
        
def divide(a,b):
    try:
       return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
       print("Number should be positive")
    except:
        print("Unexpected Erorr")  


print(divide(10,'0')) 
try:
    raise ValueError('Represents a hidden bug, do not catch this')
    #raise Exception('This is the exception you expect to handle')
except Exception as error:
    print('Caught this error: ' + repr(error))

