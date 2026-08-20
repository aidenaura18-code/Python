def total_bill(bill_amount,tip_perc):
    total = bill_amount *( 1 + 0.01 *tip_perc)
    total_bill = round(total, 2)
    print("Total bill amount is: $", total_bill)
    return total_bill



total_bill(150, 20)





def seating_arrangement(guests):
    '''this function is a recursing function'''
    if guests == 0  or guests == 1:
        return 1
    else:
        return guests * seating_arrangement(guests - 1)


print(seating_arrangement.__doc__)

print("Seating arrangements for 1 guest:", seating_arrangement(1))
print("Seating arrangements for 2 guests:", seating_arrangement(2))
print("Seating arrangements for 3 guests:", seating_arrangement(3))
print("Seating arrangements for 5 guests:", seating_arrangement(5))