# ==============================
# SMART LIBRARY & CAFÉ SYSTEM
# ==============================

from datetime import datetime

# ------------------------------
# USER CLASS
# ------------------------------
class User:
    def __init__(self, id, name="", email="", password="", loyal_points=0):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.loyal_points = loyal_points
        self.borrowed_books = []
        self.orders = []
        self.bookings = []

    def register(self):
        print("\n=== USER REGISTRATION ===")
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")

        pw1 = input("Enter a password: ")
        pw2 = input("Confirm your password: ")

        if pw1 != pw2:
            raise ValueError("❌ Passwords don't match.")
        self.password = pw1
        print(f"✅ Registration complete. Welcome, {self.name}!")

    def login(self, email, password):
        if email == self.email and password == self.password:
            print(f"✅ Welcome back, {self.name}!")
            return True
        else:
            print("❌ Invalid credentials.")
            return False

    def add_points(self, amount):
        gained = int(amount // 10)
        self.loyal_points += gained
        print(f"🎁 You earned {gained} points! Total: {self.loyal_points}")

    def show_summary(self):
        print("\n=== USER SUMMARY ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Loyalty Points: {self.loyal_points}")
        print(f"Borrowed Books: {self.borrowed_books}")
        print(f"Orders: {len(self.orders)} items")
        print(f"Bookings: {len(self.bookings)} events")

# ------------------------------
# BOOK CLASS
# ------------------------------
class Book:
    def __init__(self, title, author, category, price, copies):
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.copies = copies

# ------------------------------
# EVENT BOOKING CLASS
# ------------------------------
class EventBooking:
    def __init__(self, room, start_time, end_time, user_email):
        self.room = room
        self.start_time = start_time
        self.end_time = end_time
        self.user_email = user_email

# ------------------------------
# SMART LIBRARY & CAFÉ CLASS
# ------------------------------
class SmartLibraryCafe:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.bookings = []
        self.cafe_menu = {"Coffee": 5, "Latte": 8, "Croissant": 4}
        self.total_sales = 0

    # -------- User Management --------
    def add_user(self, user):
        if user.email in self.users:
            print("⚠️ Email already registered.")
        else:
            self.users[user.email] = user
            print("✅ User added successfully!")

    # -------- Book Management --------
    def add_book(self, book):
        self.books[book.title] = book

    def show_books(self):
        print("\n=== AVAILABLE BOOKS ===")
        if not self.books:
            print("No books in the system yet.")
            return
        for title, b in self.books.items():
            print(f"{title} | {b.author} | {b.category} | ${b.price} | Copies: {b.copies}")

    def borrow_book(self, user_email):
        user = self.users[user_email]
        self.show_books()
        title = input("Enter the title of the book to borrow: ")

        if title not in self.books:
            print("❌ Book not found.")
            return
        book = self.books[title]

        if book.copies <= 0:
            print("❌ No copies available.")
        elif len(user.borrowed_books) >= 5:
            print("⚠️ You cannot borrow more than 5 books.")
        else:
            book.copies -= 1
            user.borrowed_books.append(title)
            print(f"✅ '{title}' borrowed successfully!")

    def return_book(self, user_email):
        user = self.users[user_email]
        if not user.borrowed_books:
            print("❌ You have no borrowed books.")
            return
        print(f"Your borrowed books: {user.borrowed_books}")
        title = input("Enter the title to return: ")

        if title in user.borrowed_books:
            user.borrowed_books.remove(title)
            self.books[title].copies += 1
            print(f"✅ '{title}' returned successfully!")
        else:
            print("❌ You didn’t borrow this book.")

    # -------- Café Management --------
    def order_items(self, user_email):
        user = self.users[user_email]
        print("\n=== CAFE MENU ===")
        for item, price in self.cafe_menu.items():
            print(f"{item}: ${price}")

        total = 0
        while True:
            item = input("Enter item name (or 'done' to finish): ").capitalize()
            if item == "Done":
                break
            if item in self.cafe_menu:
                qty = int(input(f"Quantity of {item}: "))
                total += self.cafe_menu[item] * qty
            else:
                print("❌ Item not in menu.")

        if total == 0:
            print("No items ordered.")
            return

        if total > 50:
            total *= 0.9
            print("💰 10% discount applied!")

        user.orders.append(total)
        self.total_sales += total
        user.add_points(total)
        print(f"✅ Order complete! Total paid: ${total:.2f}")

    # -------- Event Booking --------
    def book_event(self, user_email):
        room = input("Enter room name: ")
        start = input("Start time (HH:MM): ")
        end = input("End time (HH:MM): ")

        # Check conflicts
        for b in self.bookings:
            if b.room == room and not (end <= b.start_time or start >= b.end_time):
                print("❌ Time slot already booked!")
                return

        booking = EventBooking(room, start, end, user_email)
        self.bookings.append(booking)
        self.users[user_email].bookings.append(booking)
        print("✅ Event booked successfully!")

    # -------- Reports --------
    def show_reports(self):
        print("\n=== SYSTEM REPORTS ===")
        if not self.users:
            print("No users yet.")
            return

        # Top 3 users by loyalty points
        top_users = sorted(self.users.values(), key=lambda u: u.loyal_points, reverse=True)[:3]
        print("\n🏆 Top 3 Users by Loyalty Points:")
        for u in top_users:
            print(f"{u.name} - {u.loyal_points} points")

        # Most borrowed book
        borrow_count = {}
        for u in self.users.values():
            for b in u.borrowed_books:
                borrow_count[b] = borrow_count.get(b, 0) + 1
        if borrow_count:
            most_borrowed = max(borrow_count, key=borrow_count.get)
            print(f"\n📚 Most Borrowed Book: {most_borrowed}")
        else:
            print("\nNo books borrowed yet.")

        print(f"\n☕ Total Café Sales: ${self.total_sales:.2f}")


# ------------------------------
# MAIN MENU FUNCTION
# ------------------------------
def main():
    system = SmartLibraryCafe()

    # Preload some books for demo
    system.add_book(Book("Python 101", "Guido van Rossum", "Tech", 20, 5))
    system.add_book(Book("Harry Potter", "J.K. Rowling", "Fiction", 15, 3))
    system.add_book(Book("Data Science Basics", "Jake VanderPlas", "Tech", 25, 2))

    while True:
        print("\n=== SMART LIBRARY & CAFÉ SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            user = User(len(system.users) + 1)
            user.register()
            system.add_user(user)

        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            if email in system.users and system.users[email].login(email, password):
                user_menu(system, email)
            else:
                print("❌ Invalid email or password.")

        elif choice == "0":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


# ------------------------------
# USER MENU FUNCTION
# ------------------------------
def user_menu(system, user_email):
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Order from Café")
        print("4. Book an Event")
        print("5. Show Profile Summary")
        print("6. Show Reports")
        print("7. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            system.borrow_book(user_email)
        elif choice == "2":
            system.return_book(user_email)
        elif choice == "3":
            system.order_items(user_email)
        elif choice == "4":
            system.book_event(user_email)
        elif choice == "5":
            system.users[user_email].show_summary()
        elif choice == "6":
            system.show_reports()
        elif choice == "7":
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid option.")


# ------------------------------
# RUN THE PROGRAM
# ------------------------------
if __name__ == "__main__":
    main()
