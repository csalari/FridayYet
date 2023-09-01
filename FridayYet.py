import datetime

print("Is it Friday yet?")

# Get the current day of the week
current_day = datetime.datetime.now().strftime("%A")

# Check if it's Friday
if current_day == "Friday":
    print("Yes!!")
elif current_day == "Thursday":
    print("Nope, it's Thursday: Just one more day, hang in there!")
elif current_day == "Monday":
    print("No, it's Monday: Fresh week, new goals!")
elif current_day == "Tuesday":
    print("No, it's Tuesday: eh...at least it's not Monday!")
elif current_day == "Wednesday":
    print("Not yet, it's Wednesday: Half-way throught the week! You got this!")
elif current_day == "Saturday":
    print("It's Saturday, which is even better! Enjoy your day!")
elif current_day == "Sunday":
    print("Nope, it's Sunday...don't let the blues get to you and set your goals for the week!")
