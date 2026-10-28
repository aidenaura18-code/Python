students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90, "Eva": 95}

for student in range(len(students)):
    average_score = sum(students.values()) / len(students)

    print(f"Average Score: {average_score}")



input_name = input("Enter the student's name to get their score: ")
if input_name in students:
    print(f"{input_name}'s score is: {students[input_name]}")

the_highest_score = max(students.values())
print(f"The highest score is: {the_highest_score}")
the_lowest_score = min(students.values())
print(f"The lowest score is: {the_lowest_score}")
