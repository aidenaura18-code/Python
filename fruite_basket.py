basket_1 = {"apple", "banana", "orange", "grape", "kiwi"}
basket_2={"banana", "kiwi", "mango", "pear"}


basket_1.add("orange")
print("Basket 1 after adding 'orange':", basket_1)


common_fruits = basket_1.intersection(basket_2)
print("Common fruits in both baskets:", common_fruits)