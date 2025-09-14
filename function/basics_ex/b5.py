#Contact book
# Ask the user to enter contacts with name as the key and phone number as the value.
# Options:
# Add a new contact
# Search for a contact by name
# Delete a contact
# Show all contacts

def get_menu_choice():
    """Display menu and get user choice."""
    print("\n" + "-"*25)
    print("STUDENT GRADE TRACKER")
    print("-"*25)
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Display all students")
    print("4. Exit")
    print("-"*25)

    
    choice = input("Choose an option (1-4): ").strip()
    return choice

def add_con(contacts): 
    pass #main logic

def del_con(contacts) :
    pass #main logic

def show_con(contacts) : 
    pass #main logic

def search_con(contacts) :
    pass #main logic

def main():
   
   contacts = {}

   print("welcome to your contact book")

   while True : 
       
       choice = get_menu_choice

       if choice == "1" : 
           add_con(contacts)
       elif choice == "2" :
           del_con(contacts)
       elif choice == "3" :
           search_con(contacts)
       elif choice == "4" :
           show_con(contacts)
       elif choice == "5" :
           break


if __name__ == "__main__":
    main()