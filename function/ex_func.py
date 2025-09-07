# Ultimate Real-Life Python Challenge: "Smart Library & Café System"

# Scenario:
# You are building a hybrid library & café management system for a small co-working space. People can borrow books, buy coffee, and even attend events. The system should track users, books, orders, and loyalty points.

# Requirements / Tasks:

# User Registration & Login

# Each user has: name, email, password, loyalty_points.

# Users can log in and log out.

# Book Management

# Store books in a dictionary: book_title: {copies_available, price, category}.

# Users can borrow a book if available (reduce copies).

# Users can return a book (increase copies).

# Track which user borrowed which books (use a dictionary).

# Café Orders

# Store menu in a dictionary: item_name: price.

# Users can order multiple items at once.

# If total order > $50, give a 10% discount.

# Each order increases the user’s loyalty_points (1 point per $10 spent).

# Events & Room Booking

# Users can book rooms for small events (time slots stored in tuples (start_time, end_time)).

# Prevent double-booking.

# Reports / Stats

# Print the top 3 users with the most loyalty points.

# Print the most borrowed book.

# Print total café sales.

# Advanced Logic

# Books can have categories (e.g., Fiction, Tech). Users can get recommendations: “users who borrowed X also borrowed Y”.

# Users cannot borrow more than 5 books at a time.

# Café menu can change dynamically (admin can add/remove items).

# Stretch Goals (optional, for ultimate challenge)

# Implement functions for every action (borrow_book, order_coffee, book_room…).

# Use sets to track unique users attending events.

# Save/load data to/from JSON files so the system remembers users, books, and sales between runs.

# Implement search functionality for books by title, category, or author.
# n=int(input("how many items do you want to enter"))

# items = []

# for i in range (n) : 
#     item = input("enter item :"  )
#     i+=1
#     items.append(item)

# print("your list of items : " , items)


items = []

print('enter your words an make stop if you want to stop')

while True : 
    item = input('enter your item' ).strip()
    if item.lower() == "stop" : 
     break
    items.append(item)

for show_item in items : 
   print(show_item)
    