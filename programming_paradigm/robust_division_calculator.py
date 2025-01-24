# Defining a funcion that performs division 
# and handles potential errors.
def safe_divide(numerator, denominator): 
    try:
        numerator=float(numerator)
        denominator=float(denominator)
        result=numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        return f"The result of the division is {result:.1f}"

