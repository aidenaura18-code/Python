class parrot:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

parrot1 = parrot("Polly", 2)
parrot2 = parrot("Kiwi", 3)

print("The name of the parrot is {} ".format(parrot1.name))
print("The age of the parrot is {} ".format(parrot1.age))
print("The name of the parrot is {} ".format(parrot2.name))
print("The age of the parrot is {} ".format(parrot2.age))
    