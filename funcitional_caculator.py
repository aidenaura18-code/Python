def add (a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    else:
        try:
            return a / b
        except:
            return "Error! Invalid input."

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")

choice = int(choice)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if  choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
    num1 + num2

         
elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
    num1 - num2

    
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
    num1 * num2 



elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
    num1 / num2