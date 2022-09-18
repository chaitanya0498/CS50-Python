# prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. 
# If the greeting starts with an “h” (but not “hello”), output `$20`. 
# Otherwise, output `$100`. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    user_input = input("Say your greetings: ")
    check(user_input)



def check(s):
    if s.lower() == "hello":
        print("$0")

    elif s.lower() == " hello ":
        print("$0")

    elif s.lower() == "hello, %":
        print("$0")

    elif s.lower().startswith("h"):
        print("$20")

    else:
        print("$100")


main()