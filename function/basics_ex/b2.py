# shopping cart manager
# Ask the user to enter items they want to buy.
# Allow them to add items to the cart.
# Allow them to remove an item if they change their mind.
# Show the current cart after each change.

# Phase 1: Structure de base (Commence par ça)
# 1. Planification des données

# Comment vas-tu stocker les articles ? (liste de strings ou dictionnaires ?)
# Exemple: ["pomme", "pain"] ou [{"item": "pomme", "quantity": 2}] ?

# 2. Menu principal
# Crée une boucle avec options :
# 1. Add item
# 2. Remove item  
# 3. Show cart
# 4. Exit
# 3. Structure de base
# pythondef main():
#     cart = []  # Ton panier
    
#     while True:
#         # afficher menu
#         # demander choix utilisateur
#         # appeler la bonne fonction
# 🛠️ Phase 2: Fonctions individuelles
# 4. Fonction add_item()

# Demander le nom de l'article
# L'ajouter au panier
# Confirmer l'ajout

# 5. Fonction remove_item()

# Afficher le panier actuel
# Demander quel article supprimer
# Le retirer du panier

# 6. Fonction show_cart()

# Afficher tous les articles
# Gérer le cas panier vide

# 🎯 Phase 3: Améliorations
# 7. Validation

# Vérifier que l'article à supprimer existe
# Gérer les entrées invalides

# 8. Fonctionnalités bonus (si tu veux)

# Quantités pour chaque article
# Prix et total
# Sauvegarder le panier

# 🚀 Questions pour démarrer :

# Par quoi veux-tu commencer ? Le menu principal ou les fonctions ?
# Format des données : Articles simples (["pomme", "pain"]) ou avec quantité ?
# Comment identifier un article à supprimer ? Par nom ou par numéro dans la liste ?

# 💡 Conseil d'approche :
# Commence TRÈS simple :

# Juste ajouter des articles (strings)
# Menu basique avec 3 options
# Une fois que ça marche → ajoute les features


# def add_item ():

# def remove_item(): 

# def show item() :


def add_item(cart): 
   while True : 
    items = input("Enter the items you want to buy or stop to exit: ")
    if items == "stop":
       break
    cart.append(items)
   print ("your cart : ") 
   show_cart(cart)


    
def remove_item(cart):
  while True:
    if not cart:
      print("your cart is empty")
      break
      
    show_cart(cart)
    removed_item = input("enter item to remove or 'done' to finish: ")
    
    if removed_item == "done":
      break
    elif removed_item not in cart:
        print("item not found in your cart")
    else:
        cart.remove(removed_item)
        print("item removed!")

   


def show_cart (cart): 
   if not cart : 
      print ("your cart is empty ")
   else:
      for item in cart:
         print(item)

def main():
  
  cart = []
  while True : 
    actions = input("Choose: 'add' (add items), 'rem' (remove items), 'show' (view cart), 'stop' (exit): ")

    if actions == "stop":
      break
    elif  actions == "add" : 
        add_item(cart)
    elif actions == "rem" :
        remove_item(cart)
    else:
       print("invalid options please choose rem , add or stop")





if __name__ == "__main__":
    main()