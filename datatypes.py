# string data type


# literal assignement
first = 'dia'
last = 'jacques'

# #common checking data type
# print(type(first))

# #check value of the variable and his data type
# print(type(last) ==  str)

# #another way to check data type
# print(isinstance(first, str))

# #constructor assignement with a function
# pizza = str('peperonni')
# print(isinstance(pizza, str))

#  #concatination 
# fullname = first + ' ' + last

# fullname += '!' 
# print(fullname)

# casting a number to a string

# decade = str(1980)

# #String methods

# print(first)
# print(first.lower())#makes all letters lowercase
# print(first.upper())#makes all letters uppercase
# print(first.title())#makes the first letter uppercase
# print(first.replace('d', 'D'))#replaces a letter with another letter
# print(first.count('a'))#counts how many times a letter appears in the string
# print(first.isalpha())#checks if all characters in the string are letters
# print(first.isalnum())#checks if all characters in the string are letters or numbers
# print(first.startswith('d'))#checks if the string starts with a specific letter
# print(first.endswith('s'))#checks if the string ends with a specific letter

# print(first)

print(" ")

#build a menu
title = "menu".upper()
print(title.center(20, "="))
print('coffee'.ljust(15, '.') + '$2.00'.rjust(5))
print('muffing'.ljust(15, '.') + '$4.00'.rjust(5))
print('cheesecake'.ljust(15, '.') + '$5.00'.rjust(5))

print(" ")

 





