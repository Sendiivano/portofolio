import random
import string

# prompt user for password length
length = int(input("Enter desired length of password: "))

# prompt user for character types
include_lowercase = input("Include lowercase letters? (y/n) ").lower() == "y"
include_uppercase = input("Include uppercase letters? (y/n) ").lower() == "y"
include_numbers = input("Include numbers? (y/n) ").lower() == "y"
include_symbols = input("Include symbols? (y/n) ").lower() == "y"

# create character set based on user input
characters = ""
if include_lowercase:
    characters += string.ascii_lowercase
if include_uppercase:
    characters += string.ascii_uppercase
if include_numbers:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# generate password
password = "".join(random.choice(characters) for _ in range(length))

# display password
print(f"Generated Password: {password}")
