# Simple calculator with match case

#Prompting the user to input two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

#Perform calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print("The result is "+str(result))
    case "-":
        result = num1 - num2
        print("The result is "+str(result))
    case "*":
        result = num1 * num2
        print("The result is "+str(result))
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("The result is "+str(result))
    case _:
        print("Invalid operator entered")