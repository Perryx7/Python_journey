# Level 1 – Review & Consolidation
# Lists + Loops
# Create a list of 5 names.
# Loop through the list using a for loop and print each name in uppercase.
# Check if a specific name (e.g., "Alice") is in the list.
# Conditions + Ternary Operator
# Ask the user for their age.
# Print "Adult" if age ≥ 18, otherwise print "Minor" (use a ternary operator).
# Operators
# Ask the user for two numbers.
# Print their sum, product, and integer division.
# Print whether the first number is even or odd (use the modulo %).


#list of 5 names
Names = ['dia', 'jacques', 'perry', 'ango', 'sohan']

for name in Names : 
    print(name.upper())

username = input("enter a name ")
 #check if the name is in the list
if username in Names :
    print(' yoir name exist ')
else:print('your name dont exist')

#age check
userage = input("enter your age ")
age= int(userage)
print("audlt") if age >= 18 else print ("minor")

nb1 = input("ente a first number ")
nb2 = input("ente a second  number ")
sum = int(nb1) + int(nb2)
print('your sum is ' + str(sum))

pro = int(nb1) * int(nb2)
print('your product is ' + str(pro))

if int(nb1) == 0 or int (nb2) == 0 : 
    print("the division is impossible give another numbers ")
else :
    div = int(nb1) / int (nb2)
    print ('your division is ' + str(div))

#even or odd
if int(nb1) and int(nb2) % 2 == 0 : 
    print("your numbers are even")
else: print("your numbers are odd")







