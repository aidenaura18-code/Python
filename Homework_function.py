def greet ():
    print("hello customer")
    print("welcome to our art store")
greet()

item=float(input("enter the price of item:"))

how_many_items=int(input("how many items you want to buy:"))

def calculate_total(item,how_many_items):
    total= item*how_many_items
    return total


Total=calculate_total(item,how_many_items)

round_total=round(Total,2)
print("your total bill is:",round_total)

amount_paid=float(input("enter the amount paid:"))

def calculate_change(amount_paid,round_total):
    change=amount_paid-round_total
    return change

change=calculate_change(amount_paid,round_total)
round_change=round(change,2)


def thank_you_message(item):
    if item>=5:
        return"great choice! you have bought more than 5 items"
    else:
        return"thank you for shopping with us"

closing =thank_you_message(how_many_items)

print(" ")
print("====bill====")
print("price of item:",item)
print("number of items:",how_many_items)
print("total bill:",round_total)
print("amount paid:",amount_paid)
print("change:",round_change)
print(closing)
print("=======")