"""
Exercise 1.1: Simple Greeting
Create a script that takes a name as an argument and greets the person.
Requirements:
•	Take one command line argument (name)
•	Print "Hello, [name]!"
•	Handle the case when no name is provided

"""


import argparse
import sys

parser = argparse.ArgumentParser(
        description="Provides a simple greetins "
    )

parser.add_argument(
        "-n",  # Short form: -n
        "--name",  # Long form: --name
        metavar="NAME",  # How the argument appears in help text
        required=False,  # This argument is mandatory
        help="The name of the person to greet"  # Description for help
    )
args = parser.parse_args()
if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Hello, stranger! Please provide your name with -n or --name.")
    sys.exit(1)

