string = input("Enter your text: ")

for _ in string:
    if _ not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        _.strip()
        print(_, end="")

print()