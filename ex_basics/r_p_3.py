
# 🟠 Level 3 – Advanced Combination
# List + Dictionary + Condition
# Create a list of dictionaries representing students with "name" and "grade".
# Loop through the list and print only students with a grade ≥ 10.
# Set + Dictionary
# Create a dictionary with products and their prices.
# Create a set with the products the customer wants to buy.
# Loop through the set and print the price for each product that exists in the dictionary.
# List + Loop + Sum
# Create a list of numbers.
# Calculate the sum of even numbers only.
# Print the result.

school = [

     {
        "name" : "dia",
        "grade" : 17
    },
   {
        "name" : "ango",
        "grade" : 16
    },
    {
        "name" : "jacques",
        "grade" : 9
    },
    {
        "name" : "perry",
        "grade" : 18
    }
]

for student in school : 
    if student["grade"] >= 10 :
        print(student["name"])

products  = {
    "apple" : 2,
    "banana" : 3,
    "orange" : 4,
    "mango" : 5}

customer_wants = {"apple","mango","grape"}
for product in customer_wants :
    if product in products : 
        print("the price of " + product + "is" + str(products[product]) )
    else: print(product + "is not available")

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0
for number in numbers : 
    if number % 2 == 0 : 
        sum =  sum  + number
        print(sum)
print("the sum of even numbers is " + str(sum))

