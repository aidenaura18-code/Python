# Floyd's Triangle
print("Floyd's Triangle:")
number = 1
for row in range(1, 6):  # 5 rows
    for col in range(row):
        print(number, end=" ")
        number += 1
    print()  # Move to next line

print("\n" + "="*30 + "\n")

# Diamond Pattern
print("Diamond Pattern:")
size = 4

# Top half (expanding)
for row in range(size):
    spaces = size - row - 1
    stars = row + 1
    print(" " * spaces + "*" * stars)

# Bottom half (contracting)
for row in range(size - 1, 0, -1):
    spaces = size - row
    stars = row
    print(" " * spaces + "*" * stars)