#  🟡 Level 2 – Introduction to Dictionaries & Sets
#  Simple Dictionary
#  Create a dictionary with 3 books, each book having "title" and "author".
#  Loop through the dictionary and print only the titles of the books.
#  Set of Unique Elements
#  Create a set with [1, 2, 2, 3, 4, 4, 5].
#  Loop through the set and print the elements.

#  Ask the user for a number and check if it is in the set.

#dictionnarie of book
book1 = {
    "name" : "name1",
    "author" : "author1"
}

book2 = {
    "name" : "name2",
    "author" : "author2"
}

book3 = {
    "name" : "name3",
    "author" : "author3"
}


#dictionnary of library with all the book
Library = {
    "book1":book1,
    "book2":book2,
    "book3":book3
}

for book in Library.values():
    print(book["author"])


nums = {1,2,2,3,4,4,5}
for num in nums:
    print(num)


number = input("enter a number")

if number in nums :
    print("your number exist")
else:print('your number dont exist')

