import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

characters = string.ascii_letters

if include_numbers:
    characters += string.digits

if include_symbols:
    characters += string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)
