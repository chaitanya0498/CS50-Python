# prompts the user for a time and outputs whether it’s `breakfast time`, `lunch time`, or `dinner time`. 
# If it’s not time for a meal, don’t output anything at all.

def main():
    user_input = input("What time is it now? ")
    time  = convert(user_input)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes


if __name__ == "__main__":
    main()