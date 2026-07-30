# Homework checklist program

tasks = ["Math", "Science", "Arabic", "Geography", "PE"]
completed = 0

print("=== Homework Checklist ===")

for task in tasks:
    while True:
        answer = input(f"Did you finish {task}? (yes/no): ").lower()
        if answer == "yes":
            completed += 1
            break
        else:
            print("Finish it first before moving on!")

print("\n=== Summary ===")
print(f"You completed {completed} out of {len(tasks)} tasks today.")

# Safe infinite loop example
print("\n=== Safe Infinite Loop Example ===")
count = 0


   
