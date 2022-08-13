import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)-to-(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if isCorrectFormat:

        pieces = isCorrectFormat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) >12:
            raise ValueError
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return first_time + ' to ' + second_time

    else:
        raise ValueError


def new_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)

    if minute == None:
        new_minute = ':00'
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute

    return new_time


if __name__ == "__main__":
    main()
