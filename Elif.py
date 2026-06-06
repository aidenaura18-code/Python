marks=92

if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("fail")





#And operator
age=20
if age >=18 and age<=60:
    print("you are eligible to work")
else:
    print("you are not eligible to work")

#Or operator
day="Sunday"
if day=="Saturday" or day=="Sunday":
    print("its a weekend")
else:
    print("its a weekday")

#not operator
raining =False
if not raining:
    print("its raining")
else:
    print("its not raining")



a=10
b=-10
c=0
if a > 0 or b > 10:
    print("either of the numbers is greater than 0")
else:
    print("neither of the numbers is greater than 0")
if  b>0 or c>0:
    print("either of the numbers is greater than 0")
else:
    print("neither of the numbers is greater than 0")