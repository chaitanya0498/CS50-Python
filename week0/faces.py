def convert(user_input):
    output = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return output

def main():
    user_input = input("Please type your text with emoticons here \n")
    print(convert(user_input))

main()