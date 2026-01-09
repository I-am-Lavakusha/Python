choice = 1

while choice != 0:
    print("\nMenu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == 0:
        print("Exiting program")

    else:
        print("Invalid choice")
