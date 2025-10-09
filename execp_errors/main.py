"""
how to handle exception and error
"""

x = 2
try:
    #print(x / 1)
    if not type(x) is str:
        raise TypeError("only strings are allowed ")
#for specific error
except NameError:
    print("NameError means something is probavly undefined.")

#to catch the zero division Error

except ZeroDivisionError:
    print("Please do not divide by zero")
    #for the type Error
except Exception as e:
    print(e)
else :
    print("No errors")
finally:
    print("i'm going to print with or without an Error")