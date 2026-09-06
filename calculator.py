print("My Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
choice = input("Choose an operation: ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
if choice == "1":
    answer = num1 + num2
    print("The answer is", answer)

elif choice == "2":
    answer = num1 - num2
    print("The answer is", answer)

elif choice == "3":
    answer = num1 * num2
    print("The answer is", answer)
else:
    print("Please choose 1, 2 or 3")