
#updultech#
def convert_seconds(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return days, hours, minutes, seconds

def main():
    user_input = int(input("++++++++++++++++++++ \nEnter time in seconds: "))
    days, hours, minutes, seconds = convert_seconds(user_input)
    print(f"{user_input} seconds is equivalent to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

if __name__ == "__main__":
    main()