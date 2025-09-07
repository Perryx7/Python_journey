#functions
def hello() : 
    print("hello world")

hello()

#function are  in lowercase and use THE 8 sepators if u nedd to separet a word
#parameters never change

# def sum(a ,b) : 
#     print(a + b)

# sum(2,3)

#a function always return something 
# def sum (a,b) :

#     return a + b

# total = sum(2,3)
# print(total)
#you can add a default value in a parameter

def sum (a, b=2) :
    if(type(a) is not int or type(b) is not int):
        return
    return a + b

total = sum(2)
print(total)

#mutiple arguments 
def multiple_items(*args) : 
    print(args)
    print(type(args))

multiple_items("dave", 'john')

#kwargs for key key words arguments and the type is dictionnary
def mult_named_items(**kwargs) : 
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = 'dave' , last = 'gray')
