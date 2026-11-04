books=["moby duck", "the great gatsby", "to kill a mockingbird", "1984", "pride and prejudice"]

copy_counts=[3, 5, 2, 4, 6]


libary = {book: count for book, count in zip(books, copy_counts)}
print("Library inventory:", libary)

available_books=[book for book in books if libary[book]>0]
print("Available books:", available_books)


chosen_blocks=input("Enter the book you want to check: ")




if chosen_blocks not in libary or libary[chosen_blocks]==0:
    print(f"Sorry, {chosen_blocks} is out of stock.")
    exit()

late_fees=[1, 2, 1.5, 2.5, 3]
extra_fee=int(input("Enter the extra fee percentage:"))


updated_fees=list(map(lambda x: x + extra_fee, late_fees))
print("Updated late fees:", updated_fees)

book_index=books.index(chosen_blocks)
print(f"The late fee for '{chosen_blocks}' is: ${updated_fees[book_index]:.2f}")

chosen_book_fee=updated_fees[book_index]
print(f"The late fee for '{chosen_blocks}' is: ${chosen_book_fee:.2f}")


libary[chosen_blocks] -= 1

print(chosen_blocks, "has been checked out. Remaining copies:", libary[chosen_blocks])

print("Updated library inventory:", libary)
print("late fees for all books:", updated_fees)
print("updated late fees for all books:", updated_fees)
print("Goodbye!")