def main():

    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars_without_sign = float(d.replace("$", ""))
    return dollars_without_sign


def percent_to_float(p):
    percentage_without_sign = float(p.replace("%", ""))
    return percentage_without_sign/100


main()
