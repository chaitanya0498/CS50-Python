# create a dictionary menu
# set current price to 0
# loop forever
# try:
    # take user input to place the order
    # check if item in the dictionary menu:
        #add the item price to current price
        #print the current price


# except: EOFError:
    # print a new line and stop the loop
    # if user inputs ctrl + d, break the loop






# create a dictionary menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# set current price to 0
total = 0
# loop forever
while True:
    try:
    # take user input to place the order
        item = input("Item: ").title()
    # check if item in the dictionary menu:
        if item in menu:
            #add the item price to current price
            total += menu[item]
            #print the current price
            print("Total: $", end="")
            print("{:.2f}".format(total))

    except EOFError:
        print()
        break