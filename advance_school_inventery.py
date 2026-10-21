items=["pencil","eraser","sharpener","notebook","glue"]
stocks=[12,0,5,3]


inventory={items:count for items, count in zip(items,stocks)}
print("full inventory:",inventory)



in_stock_items=[items for items in items if inventory[items]>0]
print("Items in stock:",in_stock_items)



chosen_item=input("Enter the item you want to check: ")
if chosen_item not in inventory or inventory[chosen_item]==0:
    print(print(f"Sorry, {chosen_item} is out of stock."))

    exit()



price=[10,5,3,20,15]
mark_up=int(input("Enter the markup percentage:"))

marked_up_prices=list(map(lambda x: x + mark_up,price))
