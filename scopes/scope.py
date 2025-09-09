# #global scope :  were a vaariable is availabe inside an outside a function

# name = "dave"

# def gretteing() : 
#     print (name)#here we can acces to name even if wi didin't declare it in a variable
#     # functio have a local scope

# def gretting() :
#     color = "blue"

# print(color)# here the terminal will give the error color not defined beacause it is in the olocal scpe of the function and we ry to accees him outside the function

#you can define a function inside another function
#the local scope of the parent become the parent scope 
#use the keyboard global to modify the the global variable inside the local space of a function otherwise you are just declare another variable


count =  1

def another() :
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name) :
        print(color)
        print(name)

    greeting("dave")

another()