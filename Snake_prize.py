from ast import Continue


def calculator_change(paid,price):
    change = paid - price
    return change

snack_prize= 25 
print(f"this snack costs {snack_prize} unites")
print("Accepted coins are 1,5,10,25\n")

total_insterted = 0
coins_inserted = 0

while True :
    coins = int(input("Insert a coin (1,5,10,25): "))
    if coins != 1 and coins != 5 and coins != 10 and coins != 25:
     print ('Invalid coin, try again')
     Continue


    total_insterted += coins
    coins_inserted += 1
    print(f"insterted {coins} .  Total so far : inserted {total_insterted}\n")


    if total_insterted >= snack_prize:
       print ("enough money inserted\n")
       break


change_due = calculator_change(total_insterted,snack_prize)
print("Dispensing snack...\n")


if change_due > 0:
       pass
else:
    print("f/Here is your change: {change_due} unites")

print("Snack dispensed:", snack_prize)
print(coins_inserted, "coins inserted")
print("total paid ", total_insterted)
print("change given ", change_due)
print("Thank you for your purchase!")