#prompts the user for input and then outputs that same input, replacing each space with `...`

string = input("Type your text here \n")

slowed_string = string.replace(" ", "...")

print(slowed_string)
