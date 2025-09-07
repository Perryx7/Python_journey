# Create a dictionary with 'book_title': copies_available.
# Create a set of book titles that students want to borrow.
# - If the book exists and copies are available, print 'Borrowed: <book>' and decrease the number of copies by 1.
# - If the book does not exist, print 'Not available: <book>'.
# At the end, print the updated library stock.



books = {
    "title1" : 5,
    "title2" : 6,
    "title3" : 1,
    "title4" : 1,
    "title5" : 0,

}

#set of title book that user want
book_title = {'title1', 'title2', "title6"}

for title in book_title : 
   if title in books:
      print(title + 'is avalaible')
      #decrease the number of copies for the book available
      books[title] -= 1
   else: print("check another book")


#remaining stock
print("the remaining stock is")

#use items() to access the Pairs of value
for title, copies in books.items() :
   
   print(title, copies)

