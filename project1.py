
while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilometers to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Thank you!")
        break

    elif choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)
            elif choice == "2":
                print("Result:", num1 - num2)
            elif choice == "3":
                print("Result:", num1 * num2)
            elif choice == "4":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Cannot divide by zero")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == "5":
        try:
            km = float(input("Enter kilometers: "))
            print("Miles:", round(km * 0.621371, 2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == "6":
        try:
            celsius = float(input("Enter Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print("Fahrenheit:", round(fahrenheit, 2))
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice! Please select from 1 to 7.")
