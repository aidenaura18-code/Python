medical_causes = input("did you have a medical cause? Y/N: ").strip().upper()
if medical_causes == 'Y':
    print("you are allowed ")
else:
    atten= int(input("how many days of attendance do you have? "))

    if atten >= 75:
        print("Allowed")
    else:
        print("Not Allowed")

age= int(input("Enter your age: "))
if age >= 18:
    if age >= 60:
        print("senior citizen")
    else:
        print("adult")
else:
    print("minor")