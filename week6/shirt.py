import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    #openthe image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    #open shirt
    shirtfile = Image.open("shirt.png")
    #get the size of the shirt
    size = shirtfile.size
    #resize the muppet image to fit the shirt
    muppet = ImageOps.fit(imagefile, size)
    #paste shirt omn muppet
    muppet.paste(shirtfile, shirtfile)
    #create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    #check how many CLelements
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    #check if an image file
    if(check_extension(file1[1])) == False:
        sys.exit("invalid input")
    if (check_extension(file2[1])) == False:
        sys.exit("invalid output")

    #check if extension of both files are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()