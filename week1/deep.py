#prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. 
# Otherwise output `No`.
user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? " ).lower().strip()

if user_input == "42":
    print("Yes")

elif user_input == "forty two":
    print("Yes")

elif user_input == "forty-two":
    print("Yes")

else:
    print("No")
