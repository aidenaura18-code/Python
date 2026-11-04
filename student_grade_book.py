grades = {
    "Alice": 92,
    "Ben": 85,
    "Chloe": 97,
    "Daniel": 78,
    "Emma": 89
}

total = 0
for score in grades.values():
    total += score

class_average = total / len(grades)
print("Class average:", class_average)

top_name = ""
top_score = 0
for name, score in grades.items():
    if score > top_score:
        top_name = name
        top_score = score

print("Highest scorer:", top_name, "-", top_score)

student_name = input("Enter a student name: ")
print(grades.get(student_name, "Not found"))