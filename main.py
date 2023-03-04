# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from os import listdir
from os.path import join , isfile
import calendar


class Weather:

    def __init__(self, year, month, days):
        self.year = year
        self.month = month
        self.days = days

    def monthly_highest_temperature(self):
        max = -1
        for day_no , day in enumerate(self.days):

            if day[0] != "":

                if day[0] > max:
                    max = day[0]

        return [max, day_no, self.month]

    def monthly_most_humid_day(self):
        max = -1
        for day_no,day in enumerate(self.days):
            if day[7] != "":
                if day[7] > max:
                    max = day[7]

        return [max, day_no, self.month]

    def monthly_lowest_temperature(self):
        min = 999
        for day_no,day in enumerate(self.days):
            if day[1] != "":
                if day[1] < min:
                    min = day[1]

        return [min,day_no,self.month]


weather_data = []


def parser(file_path):

    files_list= listdir(file_path)

    for file in files_list:

        if isfile(join(file_path,file)):
            with open(join(file_path,file),mode='r') as reader:

                days = []
                lines = reader.readlines()
                year = lines[1].split('-')[0]
                month = lines[1].split('-')[1]

                for line_no,line in enumerate(lines):

                    if line_no == 0:
                        pass
                    else:
                        values = line.replace('\n','').split(',')[1:]
                        temp = []

                        for value in values:
                            try:
                                temp.append(int(value))
                            except:
                                try:
                                    temp.append(float(value))
                                except:
                                    temp.append(value)

                        days.append(temp)

                # if(year=='2008' and month=='12'):
                #
                #     print(days)
                weather_data.append(Weather(year, month, days))


def find_highest_in_year():
    max_temp = -1
    day = ""
    month = ""
    values = []

    for data in weather_data:

        if data.year == sys.argv[2]:
            values = data.monthly_highest_temperature()

            if values[0] > max_temp:
                max_temp = values[0]
                day = values[1]
                month = values[2]

    print(f"Highest: {max_temp}C on {calendar.month_abbr[int(month)]} {day}")


def find_most_humid_in_year():
    max_temp = -1
    day = ""
    month = ""
    values = []

    for data in weather_data:

        if data.year == sys.argv[2]:
            values = data.monthly_most_humid_day()

            if values[0] > max_temp:
                max_temp = values[0]
                day = values[1]
                month = values[2]

    print(f"Humidity: {max_temp}% on {calendar.month_abbr[int(month)]} {day}")

def find_lowest_in_year():
    min_temp = 999
    day = ""
    month = ""
    values = []

    for data in weather_data:

        if data.year == sys.argv[2]:
            values = data.monthly_lowest_temperature()

            if values[0] < min_temp:
                min_temp = values[0]
                day = values[1]
                month = values[2]

    print(f"Highest: {min_temp}C on {calendar.month_abbr[int(month)]} {day}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser('/home/faran/Downloads/weatherfiles (1)/weatherfiles')

    if sys.argv[1] == '-e':
        find_highest_in_year()
        find_lowest_in_year()
        find_most_humid_in_year()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
