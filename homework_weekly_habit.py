habit_info=("reading",True,7,20.5)
print("Habit name:", habit_info)    


weekly_habit = (1, 1, 0, 1, 1, 0, 1)

print("Weekly habit tracking:", weekly_habit)


print("Days completed:", len(weekly_habit))

print("Days 1 :", weekly_habit[0])
print("Days 2 :", weekly_habit[1])
print("Days 3 :", weekly_habit[2])
print("Days 4 :", weekly_habit[3])
print("Days 5 :", weekly_habit[4])
print("Days 6 :", weekly_habit[5])
print("Days 7 :", weekly_habit[6])

first_three_days = weekly_habit[0:3]

weekly_habit_list = list(weekly_habit)

print("Weekend habit tracking:", weekly_habit_list)


weekly_habit =weekly_habit + (1,)

print("Updated weekly habit tracking:", weekly_habit)

completed_days = weekly_habit.count(1)
missed_days = weekly_habit.count(0)

print("Completed days:", completed_days)
print("Missed days:", missed_days)

done = 0
not_done = 0

for i in range(len(weekly_habit)):
    if weekly_habit[i] == 1:
        done += 1
    else:
        not_done += 1

if done > not_done:
    print("Good job! You completed your habit more than you missed it.")
else:
    print("Keep trying! You missed your habit more than you completed it.")
print("Total days completed:", done)    
print("Total days missed:", not_done)
print("Total days tracked:", len(weekly_habit))
print("Percentage of days completed:", (done / len(weekly_habit)) * 100, "%")
print("Percentage of days missed:", (not_done / len(weekly_habit)) * 100, "%")
print("Average days completed per week:", done / (len(weekly_habit) / 7))
print("Average days missed per week:", not_done / (len(weekly_habit) / 7))
print("Average days tracked per week:", len(weekly_habit) / 7)
print("Average percentage of days completed per week:", (done / len(weekly_habit)) * 100 / (len(weekly_habit) / 7), "%")
print("Average percentage of days missed per week:", (not_done / len(weekly_habit)) * 100 / (len(weekly_habit) / 7), "%")
print("Average percentage of days tracked per week:", (len(weekly_habit) / 7) * 100 / (len(weekly_habit) / 7), "%")
print("Average days completed per month:", done / (len(weekly_habit) / 30))
print("Average days missed per month:", not_done / (len(weekly_habit) / 30))
print("Average days tracked per month:", len(weekly_habit) / 30)
print("Average percentage of days completed per month:", (done / len(weekly_habit)) * 100 / (len(weekly_habit) / 30), "%")
print("Average percentage of days missed per month:", (not_done / len(weekly_habit)) * 100 / (len(weekly_habit) / 30), "%")
print("Average percentage of days tracked per month:", (len(weekly_habit) / 30) * 100 / (len(weekly_habit) / 30), "%")
print("Average days completed per year:", done / (len(weekly_habit) / 365))
print("Average days missed per year:", not_done / (len(weekly_habit) / 365))
print("Average days tracked per year:", len(weekly_habit) / 365)
print("Average percentage of days completed per year:", (done / len(weekly_habit)) * 100 / (len(weekly_habit) / 365), "%")
print("Average percentage of days missed per year:", (not_done / len(weekly_habit)) * 100 / (len(weekly_habit) / 365), "%")
print("Average percentage of days tracked per year:", (len(weekly_habit) / 365) * 100 / (len(weekly_habit) / 365), "%")
print("Average days completed per decade:", done / (len(weekly_habit) / 3650))
print("Average days missed per decade:", not_done / (len(weekly_habit) / 3650))
print("Average days tracked per decade:", len(weekly_habit) / 3650)
print("Average percentage of days completed per decade:", (done / len(weekly_habit)) * 100 / (len(weekly_habit) / 3650), "%")
print("Average percentage of days missed per decade:", (not_done / len(weekly_habit)) * 100 / (len(weekly_habit) / 3650), "%")
print("Average percentage of days tracked per decade:", (len(weekly_habit) / 3650) * 100 / (len(weekly_habit) / 3650), "%")    












# Create a tuple with different data types
habit_info = ("Reading", True, 7, 20.5)
print(habit_info)
 
# Create a tuple of daily habit completion
# 1 means completed, 0 means missed
weekly_habits = (1, 0, 1, 1, 0, 1, 1)
print(weekly_habits)
 
# Find the length of the tuple
print("Total days tracked:", len(weekly_habits))
 
# Access items using indexing
print("Day 1 status:", weekly_habits[0])
print("Day 4 status:", weekly_habits[3])
 
# Access a range using slicing
first_three_days = weekly_habits[0:3]
print("First three days:", first_three_days)
 
weekend_days = weekly_habits[5:7]
print("Weekend days:", weekend_days)
 
# Tuples are immutable, so we cannot directly add a new item
# But we can create a new tuple using the + operator
weekly_habits = weekly_habits + (1,)
print("After adding one more day:", weekly_habits)
 
# Count completed and missed days
completed = weekly_habits.count(1)
missed = weekly_habits.count(0)
 
print("Completed days:", completed)
print("Missed days:", missed)
 
# Check each day using indexing
done = 0
not_done = 0
 
for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1
 
if done > not_done:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")
 
# Final habit tracker summary
print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", habit_info[0])
print("Weekly Record:", weekly_habits)
print("Completed:", done)
print("Missed:", not_done)
print("================================")
