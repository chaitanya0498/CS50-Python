import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_2014.csv'

def parsing_CSV_file_headers():
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        #print(header_row)
    return filename


def printing_headers_and_positions():
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        #for index, column_header in enumerate(header_row):
            #print(index, column_header)


#get dates, high, and low temperatures from file

dates, highs, lows = [], [], []


def extracting_and_reading_data():
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
            #print(highs)
            #print(lows)


def plotting_data_in_temperature_chart():
    # plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    #shading an area in the chart
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # format plot
    title = "Daily High and Low Temperatures" #to add user input to the string, based on the file the user selects
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=12)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=12)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()


def main():
    parsing_CSV_file_headers()
    printing_headers_and_positions()
    extracting_and_reading_data()
    plotting_data_in_temperature_chart()


if __name__ == "__main__":
    main()
