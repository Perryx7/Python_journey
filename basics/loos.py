#while loop

# value = 1
# while value <= 10 :
#     print(value)
#     if value == 5 :
#         break
#     value += 1 


# while value <= 10 :
#     value += 1
#     if value == 5 :
#         continue
#     print(value)

# else : #when the loop uis full comlplete
#      print("value is now equal to "  + str(value))
        
     
#for loop

names = ['dave', 'sarah' , 'john']

# for name in names : 
#     print(name)

# for name in names :
#     if name == 'sarah' :
#         continue
#     print(name) 

# for loops with range

# for x in range(4) : 
#     print(x)

# for x in range(2,4) : 
#     print(x)

# for x in range(0, 100, 5):
#     print(x)

names = ['dave', 'sarah' , 'john']
actions = ["codes" , "eats" , "sleeps"]

# for name in names :
#     for action in actions:
#         print(name + "" + action + ".") 

for action in actions :
    for name in names:
        print(name + "" + action + ".") 