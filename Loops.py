# Python Loops

## 1. For Loop


for i in range(5):
    print(i)


## 2. For Loop with List


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


## 3. For Loop with Range


for i in range(1, 6):
    print(i)


## 4. Range with Step


for i in range(0, 11, 2):
    print(i)


## 5. Reverse For Loop


for i in range(10, 0, -1):
    print(i)


## 6. While Loop


i = 1

while i <= 5:
    print(i)
    i += 1


## 7. While Loop with Input


password = ""

while password != "1234":
    password = input("Enter password: ")

print("Correct password!")

## 8. Break


for i in range(1, 10):
    if i == 5:
        break

    print(i)


## 9. Continue


for i in range(1, 6):
    if i == 3:
        continue

    print(i)


## 10. Pass


for i in range(5):
    pass

print("Done")


## 11. Nested For Loop


for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

## 12. Nested While Loop


i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1


## 13. Loop Through a String


name = "Rahul"

for letter in name:
    print(letter)

## 14. Loop Through Dictionary


student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

for key in student:
    print(key)


## 15. Dictionary Keys and Values


student = {
    "name": "Rahul",
    "age": 20
}

for key, value in student.items():
    print(key, value)


## 16. Enumerate


fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


## 17. For Loop with Else


for i in range(5):
    print(i)
else:
    print("Loop finished")


## 18. While Loop with Else


i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop finished")


## 19. Break with While Loop


i = 1

while i <= 10:
    print(i)

    if i == 5:
        break

    i += 1


## 20. Infinite While Loop


while True:
    print("Hello")


## 21. Infinite Loop with Break


while True:
    number = int(input("Enter 0 to stop: "))

    if number == 0:
        break

    print(number)



## Important Loop Keywords

# break     → stops the loop
# continue  → skips the current iteration
# pass      → does nothing
# else      → runs when the loop finishes normally
# range()   → generates a sequence of numbers
# enumerate() → gives index and value