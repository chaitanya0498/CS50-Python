''' In a file called emojize.py, implement a program that
prompts the user for a str in English and then
 outputs the “emojized” version of that str,
  converting any codes (or aliases) therein to their corresponding emoji.
'''
import emoji
# prompt the user for a string in English
text = input("Text: ")

# install the emoji module
# import emoji module
# pass the string through the emojize function, import any necessary modules for that
print(emoji.emojize(text, language='alias'))



# print the output of the function

