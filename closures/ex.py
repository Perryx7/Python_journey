# LEVEL 1 EXERCISES - Basic Scope
# Exercise 1.1: Debug the scope
# pythonx = 10

# def test():
#     x = 20
#     print(f"Inside test: {x}")

# test()
# print(f"Global: {x}")
# Question: What will this code output and why?

# Exercise 1.2: Global counter
# Create a function increment_counter() that:

# Uses a global variable counter = 0
# Increments it by 1 on each call
# Prints the new value

count = 0

def incremnt_counter () :
    global count
    count += 1
    print (count)


test = incremnt_counter
test()
test()
test()
test()

# Exercise 1.3: Modify a global list
# # Write a function add_item(item) that adds to this global list
# # Write a function show_items() that displays all items
pythonitems = []

def add_items(item) :
    global pythonitems
    pythonitems.append(item)
def show_items() :
        print (pythonitems)


# 🎯 LEVEL 2 EXERCISES - Nonlocal
# Exercise 2.1: Counter with nonlocal
# Create a function that returns another function:
# pythondef make_counter():
#     # Local variable here
#     def increment():
#         # Use nonlocal to modify parent's variable
#         pass
    
#     return increment
def make_counter() :
     counter = 0

     def increment ():
          nonlocal counter 
          counter +=1

     return increment

test = make_counter()
test()


# Exercise 2.2: Calculator with memory
# pythondef make_calculator():
#     # Variable to store previous result
    
#     def calculate(operation, number):
#         # Use nonlocal to modify result
#         # Support: 'add', 'multiply', 'reset'
#         pass
    
#     return calculate


def make_calculator ():
     result = 0

     def calculate(operation, number) :
          nonlocal result 
          if operation == "add" : 
               result += number 
          elif operation == "multiply" :
               result *= number
          elif operation == "reset" :
               result = 0
               return result

     return calculate


calc = make_calculator()
calc("add" , 5)
calc("add" , 5)
calc("multiply" , 5)




# Exercise 2.3: Connection state
# pythondef make_connection_manager():
#     # Variable for state (True/False)
    
#     def connect():
#         # Change state to True, but only if False
#         pass
    
#     def disconnect():
#         # Change state to False, but only if True
#         pass
    
#     def status():
#         # Return current state
#         pass
    
#     return connect, disconnect, status

# 🚀 LEVEL 3 EXERCISES - Advanced Closures
# Exercise 3.1: Validator factory
# pythondef make_validator(min_length, max_length):
#     # Create a function that validates if a string 
#     # is between min_length and max_length
#     pass

# # Usage:
# # email_validator = make_validator(5, 50)
# # password_validator = make_validator(8, 20)
# Exercise 3.2: Call history tracker
# pythondef track_calls(func):
#     # Create a wrapper function that:
#     # - Counts how many times func has been called
#     # - Stores arguments from each call
#     # - Can display the history
#     pass

# # Usage:
# # tracked_func = track_calls(my_function)
# Exercise 3.3: Rate limiter
# pythondef make_rate_limiter(max_calls, time_window):
#     # Limit number of calls within a time window
#     # max_calls: maximum number of calls
#     # time_window: window in seconds
#     pass

# # Usage:
# # limiter = make_rate_limiter(3, 60)  # 3 calls per minute
# # limiter()  # OK
# # limiter()  # OK  
# # limiter()  # OK
# # limiter()  # "Rate limit exceeded"

# 💪 LEVEL 4 EXERCISES - Challenges
# Exercise 4.1: Cache with expiration
# pythondef make_cache(expiry_seconds):
#     # Create a cache that:
#     # - Stores key-value pairs
#     # - Expires them after expiry_seconds
#     # - Returns None if expired
#     pass

# # Usage:
# # cache = make_cache(30)  # 30 seconds
# # cache.set("key", "value")
# # cache.get("key")  # "value" if not expired
# Exercise 4.2: Game state manager
# pythondef make_game_state():
#     # Create a state manager for a game with:
#     # - score, level, lives
#     # - Functions: add_score, level_up, lose_life, reset
#     # - Function get_state that returns all state
#     pass
# Exercise 4.3: Builder pattern
# pythondef make_user_builder():
#     # Builder pattern to create a user
#     # Chainable methods: name(), age(), email(), build()
#     pass

# # Usage:
# # builder = make_user_builder()
# # user = builder.name("Alice").age(25).email("alice@test.com").build()

# 🎯 BONUS - Practical Exercises
# Bonus Exercise 1: Configuration manager
# Create a configuration system with closures that can:

# Store configurations by environment (dev, prod, test)
# Allow hot reloading
# Keep history of changes

# Bonus Exercise 2: Event system
# Implement an event system with:

# Callback registration
# Event triggering
# Shared state between all listeners


# 💡 Tips for solving:

# Start with exercises 1.x to understand basics
# Draw the scopes on paper if confused
# Use print() everywhere for debugging
# global = variable defined outside all functions
# nonlocal = variable in parent function
# closure = function that "captures" variables from its environment



