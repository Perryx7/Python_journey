# Shopping cart manager
# Ask the user to enter items they want to buy.
# Allow them to add items to the cart.
# Allow them to remove an item if they change their mind.
# Show the current cart after each change.

def add_item(cart): 
    while True: 
        item = input("Enter the item to add (or 'stop' to return to menu): ").strip().lower()
        if item == "stop":
            break
        cart.append(item)
        print(f"'{item}' added to your cart!")
        show_cart(cart)

def remove_item(cart):
    while True:
        if not cart:
            print("Your cart is empty.")
            break
        
        show_cart(cart)
        removed_item = input("Enter item to remove (or 'done' to return to menu): ").strip().lower()
        
        if removed_item == "done":
            break
        elif removed_item not in cart:
            print(f"'{removed_item}' not found in your cart.")
        else:
            cart.remove(removed_item)
            print(f"'{removed_item}' removed from your cart!")
            show_cart(cart)

def show_cart(cart): 
    if not cart: 
        print("Your cart is empty.")
    else:
        print("\n🛒 Current cart:")
        for item in cart:
            print(f" - {item}")
        print()

def main():
    cart = []
    while True: 
        action = input("Choose: 'add', 'rem', 'show', 'stop': ").strip().lower()

        if action == "stop":
            print("\nFinal cart before exit:")
            show_cart(cart)
            break
        elif action == "add": 
            add_item(cart)
        elif action == "rem":
            remove_item(cart)
        elif action == "show":
            show_cart(cart)
        else:
            print("Invalid option. Please choose: add, rem, show, stop.")

if __name__ == "__main__":
    main()
