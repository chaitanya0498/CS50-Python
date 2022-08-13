# create a list to store the names entered
import inflect
p = inflect.engine()

names = []

# infinite loop
while True:
    try:
        #get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        #create new line and stop the loop
        print()
        break

output = p.join(names)
print("Adieu, adieu, to " + output)

# print using inflect module