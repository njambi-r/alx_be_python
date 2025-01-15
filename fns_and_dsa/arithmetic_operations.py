def perform_operation(num1, num2, operation):
    if operation=="add":
        result=num1+num2
    elif operation=="subtract":
        result=num2-num1
    elif operation=="multiply":
        result=num1*num2
    elif operation=="divide":
        if num2==0:
           result=print ("Cannot divide bu zero")
        else:
           result=num1/num2
    return result
    