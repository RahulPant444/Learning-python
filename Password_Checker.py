import re

password = input("Enter your password: ")

length_ok = len(password) >= 8

uppercase = bool(re.search(r"[A-Z]", password))
lowercase = bool(re.search(r"[a-z]", password))

numbers = bool(re.search(r"\d", password))

special = bool(re.search(r"[^A-Za-z0-9]", password))


score = sum([length_ok, uppercase, lowercase, numbers, special])

if score <= 2:
    strength = "Weak"
elif score == 3 or score == 4:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Analysis")
print("-----------------")
print("Length >= 8:       ", "Yes" if length_ok else "No")
print("Uppercase:         ", "Yes" if uppercase else "No")
print("Lowercase:         ", "Yes" if lowercase else "No")
print("Numbers:           ", "Yes" if numbers else "No")
print("Special character: ", "Yes" if special else "No")
print("Strength:           ", strength)
