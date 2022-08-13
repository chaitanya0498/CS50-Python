import sys
import csv

def main():
    #check command line arguments
    check_command_line_arg()
    output = []

    #try to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({'first': split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
            #create name, last name
            #add them to the dict


    #if unable to open, the file doesn't exist
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")




    #write to a new csv file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
            writer.writerow({"first": "first", "last": "last", "house": "house"})

def check_command_line_arg():
    #check how many elements the the commang line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #check if it's a csv file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()

