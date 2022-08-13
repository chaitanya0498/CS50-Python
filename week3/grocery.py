# start  an infinite loop

groceries = {}

while True:

    try:

        # prompt user for item
        item = input().lower()

        if item in groceries:
            groceries[item] += 1

        else:
            groceries[item] = 1


    except EOFError:

        for key in sorted(groceries.keys()):
            print(groceries[key], key.upper())


        break



# output user's imput in all uppercase sorted aphabetically