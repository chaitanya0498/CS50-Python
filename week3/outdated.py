# create list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# start an infinite loop
while True:


    # prompt user for a date (AD) in MDY order
    date = input("Date: ")

    try:
        # split the date by slashes

        month, day, year = date.split("/")


        # check if month lies between 1-12 and days 1-31

        if (int(month) >= 1 and int(month) <= 12) and (int(day) >=1 and int(day) <= 31):
            break



    except:

        try:

            #split the date by spaces (MMDDYYY)
            old_month, old_day, year = date.split(" ")

            #find the number for the month

            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1 #indexing from 0 converted to 1

            #remove comma from day variable

            day = old_day.replace(",", "")

            #check if month lies between 1-12 and days 1-31

            if (int(month) >= 1 and int(month) <=12) and (int(day) >=1 and int(day) <= 31):
                break



        except:

            #move to the next line
            print()
            pass

#if month and is less than 10, add a 0 digit to the left

#print the result
print(f"{year}-{int(month):02}-{int(day):02}", end="")

# output the date in YYYY-MM-DD format

# if user input is invalid in either format, prompt again
