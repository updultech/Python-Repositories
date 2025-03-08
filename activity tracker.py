class ActivityTracker:
    def __init__(self):
        self.activities = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }

    def add_activity(self):
        day = input("Enter the day (Monday-Sunday): ")
        activity = input("Enter the activity: ")
        self.activities[day].append(activity)
        print(f"Activity added for {day}!")

    def view_activities(self):
        day = input("Enter the day (Monday-Sunday): ")
        print(f"Activities for {day}:")
        for activity in self.activities[day]:
            print(activity)

    def delete_activity(self):
        day = input("Enter the day (Monday-Sunday): ")
        activity = input("Enter the activity to delete: ")
        if activity in self.activities[day]:
            self.activities[day].remove(activity)
            print(f"Activity deleted for {day}!")
        else:
            print("Activity not found!")

def main():
    tracker = ActivityTracker()
    while True:
        print("1. Add Activity")
        print("2. View Activities")
        print("3. Delete Activity")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            tracker.add_activity()
        elif choice == "2":
            tracker.view_activities()
        elif choice == "3":
            tracker.delete_activity()
        elif choice == "4":
        	break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()