# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an undefined priority."

if time_bound == "yes" and priority in ("high", "medium"):
    reminder = reminder.rstrip('.') + " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    reminder = reminder.rstrip('.') + ". Consider completing it when you have free time."

print(reminder)
