try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    result=num1/num2

except ValueError:
    print("you must enter numbers only")
except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print(result)

finally:
    print("the program is completed")

