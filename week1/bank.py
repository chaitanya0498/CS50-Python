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