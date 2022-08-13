while True:
    #prompt user for input
    fraction = input("Fraction: ")

    try:

        #check if it's in the correct format x/y fraction

        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        #convert the fraction to integer
        fuel = x/y
        # print(fuel)

        if fuel <= 1:
            break

    except(ValueError, ZeroDivisionError):
        pass

# multiply fuel by 100 to get percentage
fuel_p = fuel * 100
f = round(fuel_p)

#as per the specifications
if f <= 1:
    print("E")
elif f >= 99:
    print("F")
else:
    print(f, "%", sep="", end="")


