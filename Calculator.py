import math

def calculator():
    print("=== Python Calculator ===")
    print("1. Basic Operations")
    print("2. Percentage")
    print("3. Power / Square Root")
    print("4. Function and Condition")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            print("Result:", a + b)
        elif operator == "-":
            print("Result:", a - b)
        elif operator == "*":
            print("Result:", a * b)
        elif operator == "/":
            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", a / b)
        else:
            print("Invalid operator.")

    elif choice == "2":
        percentage = float(input("Enter percentage: "))
        number = float(input("Enter number: "))

        result = (percentage / 100) * number
        print(f"{percentage}% of {number} =", result)

    elif choice == "3":
        print("1. Power")
        print("2. Square Root")

        operation = input("Choose operation: ")

        if operation == "1":
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))

            print("Result:", base ** exponent)

        elif operation == "2":
            number = float(input("Enter number: "))

            if number < 0:
                print("Error: Square root of a negative number.")
            else:
                print("Result:", math.sqrt(number))

        else:
            print("Invalid choice.")

    elif choice == "4":
        x = float(input("Enter x: "))

        def f(x):
            return 2 * x + 5

        print("f(x) =", f(x))

        # Condition
        if x > 10:
            print("Condition: Large")
        elif x == 10:
            print("Condition: Equal")
        else:
            print("Condition: Small")

    else:
        print("Invalid choice.")


calculator()