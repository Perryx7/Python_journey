"""
- A lambda function is  single function that return a value

"""
#import sys

# method to declare a lambda function
squared = lambda num: num * num

print(squared(4))

addTwo = lambda num: num + 2
print(addTwo(4))

#lambda can except more than one parameter

var = lambda a, b: a + b
print(var(4, 5))


###
def funcbuilder(x):
    return lambda num: num + x


addTen = funcbuilder(10)
addTwenty = funcbuilder(20)

print(addTwenty(10))
print(addTen(20))

"""
   Higher order function : 
    - is a function that takes one or more function as argument or a function that return other function as result

"""
squared = lambda num : num **2

numbers = [1, 2, 3, 4, 5]

#map is a higher other function that take to parameter as here we have squared as a function and numbers who is a list and return a new list
squared_nums = map(squared, numbers)

print(list(squared_nums))

#######################################""""""

###filter

even_odd = lambda num: num % 2 != 0

##the function here will return true if it is divided by 2 and false if not

add_nums = filter(even_odd , numbers)
print(list(add_nums))

########## reduce

from functools import reduce
reduce_func= lambda acc, curr : acc + curr

numbers = [1, 2, 3, 4, 5]

total = reduce(reduce_func, numbers, 10)
print(total)


#seccond usage of reduce

string_reduce = lambda acc, curr : acc + len(curr)

names = ["dave" ,"jacques" , "sarah" , "sohan"]

char_count = reduce(string_reduce ,  names, 0)
print(char_count)




