# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium":
        message = f"Reminder: '{task}' is a {priority} priority task"
        if time_bound == "yes":
            message += " that requires immediate attention today!"
        else:
            message += "."
    case "low":
        message = f"Note: '{task}' is a low priority task"
        if time_bound == "no":
            message += ". Consider completing it when you have free time."
        else:
            message += "."
    case _:
        message = f"Note: '{task}' has an undefined priority."

print(message)
