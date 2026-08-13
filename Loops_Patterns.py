# ==============================
# 1. Square Pattern
# ==============================

print("\n" + "=" * 40)
print("1. Square Pattern")
print("=" * 40)

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


# ==============================
# 2. Rectangle Pattern
# ==============================

print("\n" + "=" * 40)
print("2. Rectangle Pattern")
print("=" * 40)

for i in range(3):
    for j in range(6):
        print("*", end=" ")
    print()


# ==============================
# 3. Right Triangle
# ==============================

print("\n" + "=" * 40)
print("3. Right Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# ==============================
# 4. Inverted Right Triangle
# ==============================

print("\n" + "=" * 40)
print("4. Inverted Right Triangle")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ==============================
# 5. Right-Aligned Triangle
# ==============================

print("\n" + "=" * 40)
print("5. Right-Aligned Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# ==============================
# 6. Inverted Right-Aligned Triangle
# ==============================

print("\n" + "=" * 40)
print("6. Inverted Right-Aligned Triangle")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()


# ==============================
# 7. Pyramid
# ==============================

print("\n" + "=" * 40)
print("7. Pyramid")
print("=" * 40)

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


# ==============================
# 8. Inverted Pyramid
# ==============================

print("\n" + "=" * 40)
print("8. Inverted Pyramid")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


# ==============================
# 9. Diamond
# ==============================

print("\n" + "=" * 40)
print("9. Diamond")
print("=" * 40)

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()


# ==============================
# 10. Hollow Square
# ==============================

print("\n" + "=" * 40)
print("10. Hollow Square")
print("=" * 40)

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ==============================
# 11. Hollow Rectangle
# ==============================

print("\n" + "=" * 40)
print("11. Hollow Rectangle")
print("=" * 40)

for i in range(4):
    for j in range(7):
        if i == 0 or i == 3 or j == 0 or j == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ==============================
# 12. Number Triangle
# ==============================

print("\n" + "=" * 40)
print("12. Number Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==============================
# 13. Same Number Triangle
# ==============================

print("\n" + "=" * 40)
print("13. Same Number Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# ==============================
# 14. Inverted Number Triangle
# ==============================

print("\n" + "=" * 40)
print("14. Inverted Number Triangle")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==============================
# 15. Repeated Number Pattern
# ==============================

print("\n" + "=" * 40)
print("15. Repeated Number Pattern")
print("=" * 40)

for i in range(1, 6):
    for j in range(5):
        print(i, end=" ")
    print()


# ==============================
# 16. Floyd's Triangle
# ==============================

print("\n" + "=" * 40)
print("16. Floyd's Triangle")
print("=" * 40)

num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# ==============================
# 17. Reverse Number Pattern
# ==============================

print("\n" + "=" * 40)
print("17. Reverse Number Pattern")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# ==============================
# 18. Continuous Number Pattern
# ==============================

print("\n" + "=" * 40)
print("18. Continuous Number Pattern")
print("=" * 40)

num = 1

for i in range(5):
    for j in range(5):
        print(num, end=" ")
        num += 1
    print()


# ==============================
# 19. 0-1 Pattern
# ==============================

print("\n" + "=" * 40)
print("19. 0-1 Pattern")
print("=" * 40)

for i in range(1, 6):
    for j in range(i):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()


# ==============================
# 20. Alphabet Triangle
# ==============================

print("\n" + "=" * 40)
print("20. Alphabet Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# ==============================
# 21. Same Alphabet Pattern
# ==============================

print("\n" + "=" * 40)
print("21. Same Alphabet Pattern")
print("=" * 40)

for i in range(5):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


# ==============================
# 22. Continuous Alphabet Pattern
# ==============================

print("\n" + "=" * 40)
print("22. Continuous Alphabet Pattern")
print("=" * 40)

ch = 65

for i in range(5):
    for j in range(5):
        print(chr(ch), end=" ")
        ch += 1
    print()


# ==============================
# 23. Reverse Alphabet Triangle
# ==============================

print("\n" + "=" * 40)
print("23. Reverse Alphabet Triangle")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


# ==============================
# 24. Plus Pattern
# ==============================

print("\n" + "=" * 40)
print("24. Plus Pattern")
print("=" * 40)

n = 5

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ==============================
# 25. X Pattern
# ==============================

print("\n" + "=" * 40)
print("25. X Pattern")
print("=" * 40)

n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ==============================
# 26. Hollow Triangle
# ==============================

print("\n" + "=" * 40)
print("26. Hollow Triangle")
print("=" * 40)

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ==============================
# 27. Butterfly Pattern
# ==============================

print("\n" + "=" * 40)
print("27. Butterfly Pattern")
print("=" * 40)

n = 5

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


# ==============================
# 28. Pascal's Triangle
# ==============================

print("\n" + "=" * 40)
print("28. Pascal's Triangle")
print("=" * 40)

n = 5

for i in range(n):
    num = 1

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()


# ==============================
# 29. Hollow Pyramid
# ==============================

print("\n" + "=" * 40)
print("29. Hollow Pyramid")
print("=" * 40)

n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# ==============================
# 30. Hollow Inverted Pyramid
# ==============================

print("\n" + "=" * 40)
print("30. Hollow Inverted Pyramid")
print("=" * 40)

n = 5

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# ==============================
# 31. Number Pyramid
# ==============================

print("\n" + "=" * 40)
print("31. Number Pyramid")
print("=" * 40)

n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# ==============================
# 32. Palindrome Number Pyramid
# ==============================

print("\n" + "=" * 40)
print("32. Palindrome Number Pyramid")
print("=" * 40)

n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()


# ==============================
# 33. Character Square
# ==============================

print("\n" + "=" * 40)
print("33. Character Square")
print("=" * 40)

for i in range(5):
    for j in range(5):
        print(chr(65 + j), end=" ")
    print()


# ==============================
# 34. Character Triangle
# ==============================

print("\n" + "=" * 40)
print("34. Character Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + i - 1), end=" ")
    print()


# ==============================
# 35. Alternating 0-1 Square
# ==============================

print("\n" + "=" * 40)
print("35. Alternating 0-1 Square")
print("=" * 40)

for i in range(5):
    for j in range(5):
        print((i + j) % 2, end=" ")
    print()


# ==============================
# 36. Checkerboard Pattern
# ==============================

print("\n" + "=" * 40)
print("36. Checkerboard Pattern")
print("=" * 40)

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ==============================
# 37. Multiplication Pattern
# ==============================

print("\n" + "=" * 40)
print("37. Multiplication Pattern")
print("=" * 40)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()


# ==============================
# 38. Binary Triangle
# ==============================

print("\n" + "=" * 40)
print("38. Binary Triangle")
print("=" * 40)

for i in range(1, 6):
    for j in range(i):
        print(j % 2, end=" ")
    print()


# ==============================
# 39. Descending Number Triangle
# ==============================

print("\n" + "=" * 40)
print("39. Descending Number Triangle")
print("=" * 40)

for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()


# ==============================
# 40. Number Pyramid
# ==============================

print("\n" + "=" * 40)
print("40. Number Pyramid")
print("=" * 40)

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print(i, end=" ")

    print()


print("\n" + "=" * 40)
print("ALL 40 PATTERNS COMPLETED")
print("=" * 40)