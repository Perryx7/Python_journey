"""
A multilingual greeting script that demonstrates command line arguments.
This script takes a person's name and language preference, then prints
a greeting in the specified language.
"""


def hello(name, lang):
    """
    Function that prints a greeting in different languages.

    Args:
        name (str): The name of the person to greet
        lang (str): The language code (en, fr, sp)
    """
    # Dictionary mapping language codes to greeting words
    # This allows us to easily add new languages or modify existing ones
    greetings = {
        "en": "Hello",  # English greeting
        "fr": "Bonjour",  # French greeting
        "sp": "Hola",  # Spanish greeting
    }

    # Create the greeting message using f-string formatting
    # f"{greetings[lang]}" gets the greeting from the dictionary
    # using the language code as the key
    msg = f"{greetings[lang]} {name}!"

    # Print the final greeting message
    print(msg)


# This is a Python idiom that checks if this script is being run directly
# (not imported as a module). __name__ is a special variable that Python sets:
# - When script is run directly: __name__ == "__main__"  
# - When script is imported: __name__ == "module_name"
if __name__ == "__main__":
    # Import argparse module for handling command line arguments
    # We import it here (not at top) since it's only needed when running directly
    import argparse

    # Create an ArgumentParser object
    # This will handle parsing command line arguments and generating help text
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting in different languages"
    )

    # Add the first command line argument: --name or -n
    parser.add_argument(
        "-n",  # Short form: -n
        "--name",  # Long form: --name
        metavar="NAME",  # How the argument appears in help text
        required=True,  # This argument is mandatory
        help="The name of the person to greet"  # Description for help
    )

    # Add the second command line argument: --lang or -l
    parser.add_argument(
        "-l",  # Short form: -l
        "--lang",  # Long form: --lang
        metavar="LANGUAGE",  # How the argument appears in help text
        required=True,  # This argument is mandatory
        choices=["en", "fr", "sp"],  # Only these values are allowed
        help="The language for the greeting (en=English, fr=French, sp=Spanish)"
    )

    # Parse the command line arguments
    # This processes sys.argv and returns a namespace object with the values
    args = parser.parse_args()

    # Call our hello function with the parsed arguments
    # args.name contains the value passed to --name
    # args.lang contains the value passed to --lang
    hello(args.name, args.lang)
