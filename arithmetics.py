# Prompt the user to enter two numbers and an operator (+, -, *, /)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = input("Enter the operator(+,-,*,/): ")
if result == "+":
    print(f"Sum: ",num1 + num2)
elif result == "-":
    print(f"Difference: ",num1 - num2)
elif result == "*":
    print(f"Product: ",num1 * num2)
elif result == "/":
    if num2 != 0:
        print(f"Quotient: ",num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")
