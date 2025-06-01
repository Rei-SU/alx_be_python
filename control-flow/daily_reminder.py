# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
        if time_bound == "no":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += "."
    case _:
        reminder = f"Note: '{task}' has an undefined priority level."

print(reminder)
