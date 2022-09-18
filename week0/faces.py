#implement a function called `convert` that accepts a `str` as input and returns that same input with any `:)` converted to 🙂
#implement a function called `main` that prompts the user for input, calls `convert` on that input, and prints the result.

def convert(user_input):
    output = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return output

def main():
    user_input = input("Please type your text with emoticons here \n")
    print(convert(user_input))

main()