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
    print("CONTACT COLLECTION")
    print("-"*25)
    print("1. Add a new contact")
    print("2. search for a contact")
    print("3. Display all contacts")
    print("4. delete a contact")
    print("5. Exit")
    print("-"*25)

    
    choice = input("Choose an option (1-4): ").strip()
    return choice

def add_con(contacts): 
    
    contact_name = input("Enter a contact name :  ")
    if contact_name in contacts:
        print(contact_name + " "  +  "already exist")
    else:
        contact_num  = int(input("Enter a phone number"))
        contacts[contact_name] = contact_num
        print(contact_name + " " + " succesfuly added ")


def del_con(contacts) :
    del_con = input("Enter the name of the contact you want to delete: ")

    if del_con not in contacts : 
        print("this contact don't exist in the list")
    else : 
        contacts.pop(del_con)
        print("contact delete succesfully")

    

def show_con(contacts) : 
    if not contacts :
        print("There is no contact in the list")
    else:
        for i, contact in enumerate(contacts.items(), start=1):
         print(f"{i}. {contact}")


def search_con(contacts) :

    consearch = input("Enter a name")

    if consearch in contacts : 
        print(consearch)
    else : print("contact not find")

    pass #main logic

def main():
   
   contacts = {}

   print("welcome to your contact book")

   while True : 
       
       choice = get_menu_choice()

       if choice == "1" : 
           add_con(contacts)
       elif choice == "2" :
           search_con(contacts)
       elif choice == "3" :
           show_con(contacts)
       elif choice == "4" :
           del_con(contacts)
       elif choice == "5" :
           break


if __name__ == "__main__":
    main()