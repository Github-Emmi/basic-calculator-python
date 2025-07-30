# 🎉 Welcome to the Fun Calculator! 🎉
# We're going to add, subtract, multiply, and divide two numbers like a boss! 😎

# Python Code Example: `calculator.py`
# calculator.py

# Get user inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation entered.")


# 🏁 And that's it! You've just made a mini-calculator! 😎💻
