#Python Modules – Exercises from Easy to Pro
#Level 1 – Beginner (Basics of modules)
#•	1. Simple Import
#- Create a file greetings.py with a function say_hello(name).
#- In main.py, import greetings and call the function with your name.

#•	2. Aliasing
#- Import math as m and calculate sqrt(49) and factorial(6).
import math as m
print(m.sqrt(49))
print(m.factorial(6))
#•	3. Selective Import
# From random import only randint. Print 5 random integers between 1 and 20.
#evel 2 – Intermediate (Own modules & packages)
#•	4. Your Own Module
#- Create calculator.py with functions: add, subtract, multiply, divide.
#- Import it in main.py and test all functions.
#•	5. Using __name__ == '__main__'
#- Add a test block in calculator.py that runs only when the file is executed directly.
#•	6. Constants Module
#- Create constants.py with PI = 3.14159, E = 2.718.
#- Use it in another file to calculate area of a circle and exponential growth.
#	7. Package with Multiple Modules
# Create geometry/ with circle.py (area(radius)) and rectangle.py (area(length, width)).
#- Add __init__.py. Import and calculate areas in main.py.
#Level 3 – Advanced (Real usage)
#•	8. Built-in Modules
#- Use datetime (today’s date), os (current dir), sys (Python version), random (random number).
#•	9. File Operations with a Module
#- Create file_utils.py with read_file(path) and write_file(path, text). Test it.
#•	10. Package with Sub-Packages
#- Create ecommerce/ with cart/add.py and payment/process.py.
#- Simulate shopping in main.py.
#Level 4 – Pro (Reusable, external modules)
#•	11. Custom Exception Module
#- Create errors.py with InvalidAgeError(Exception).
#- In main.py, raise and handle when age < 0.
#•	12. Utility Package
#- Create utils/ with math_utils.py and string_utils.py.
#- Reuse in multiple projects.
#•	13. External Module
#- Install requests. Create api_client.py with get_github_user(username). Test it with your GitHub username.
#•	14. Reusable Library
#- Organize utils/ package with setup.py or pyproject.toml.
#- Install locally with pip install -e . and import in another project.
