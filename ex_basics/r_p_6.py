# Create a list of orders.
# Each order is a dictionary with 'customer' and 'items' (a dictionary of 'product': quantity).
# You also have a dictionary of product prices.
# - Loop through all orders, calculate the total bill for each customer, and print it.
# - At the end, print the grand total sales of the store.

#list of orders
orders = [
    {
        "customer" : "customer 1",
        #product and quantity
        "items" : {
            "product1" : 12,
            "product2" : 14,
            "product3" : 10,
            "product4" : 23
        }
      },

         {
        "customer" : "customer 2",
        "items" : {
            "product1" : 21,
            "product2" : 41,
            "product3" : 10,
            "product4" : 32
        }
      },

         {
        "customer" : "customer 3",
        "items" : {
            "product1" : 31,
            "product2" : 51,
            "product3" : 40,
            "product4" : 32
        }
      },

         {
        "customer" : "customer 4",
        "items" : {
            "product1" : 42,
            "product2" : 41,
            "product3" : 1,
            "product4" : 44
        }
      }
]

#dictionnaries of product-prizes
product_prize = {

    "product1": 8,
    "product2": 10,
    "product3": 28,
    "product4": 40
}



total_sales = 0#total of all the orders

for order in orders : 
  items = order["items"]#recup all the items
  total_order = 0
  print("order for " + order["customer"] + "is: ")#list all order for customer

  for item , quantity in items.items() : 
      
      price = product_prize[item]#recup the prize of each item
      p_price = price * quantity
 
      print(item +":" +  str(price * quantity))
      total_order += p_price
      total_sales += total_order 

  print("the total of the orders is  " + str(total_order))
  print("the total sales is " + str(total_sales))






