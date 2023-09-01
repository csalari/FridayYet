import datetime

print("Is it Friday yet?")

# Get the current day of the week
current_day = datetime.datetime.now().strftime("%A")

# Check if it's Friday
if current_day == "Friday":
    print("Yes!!")
elif current_day == "Thursday":
    print("Just one more day, hang in there!")
else:
    print("Sorry, no.")