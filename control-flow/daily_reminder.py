# daily_reminder.py
# A simple task reminder based on priority and time sensitivity

def main():
    print("Welcome to your Daily Task Reminder!")
    
    # Get user input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Validate priority input
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower()
    
    # Validate time-bound input
    while time_bound not in ['yes', 'no']:
        print("Please answer with yes or no.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Process based on priority using match case
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. You should focus on this soon.")
        
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a medium priority task with a deadline. Try to complete it today.")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Schedule time for it this week.")
        
        case 'low':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a low priority task but has a deadline. Complete it when possible.")
            else:
                print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()