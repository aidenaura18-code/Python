def add (a, b):
    return a + b
    


def subtract (a, b):
    return a - b


def multiply (a, b):
    return a * b


def divide (a, b):
    return a / b
        
    

num1 = float(input("Enter a number 1: "))
num2 = float(input("Enter a number 2: "))
operation = input("enter operation:  + for add, - for subtract, * for multiply, / for divide: ")



if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    print("Invalid operation")
try:
    zero_division = divide(num1, num2)
    print("Division result is:", zero_division)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


print(operation, "result is:", result)


