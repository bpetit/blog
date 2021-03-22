#!/usr/bin/env python3

import csv
from pprint import pprint

def main ():

    with open('google_data.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        avg = 0
        nb = 0
        for row in reader:
            print(row['Grid carbon intensity (gCO2eq / kWh)'])
            avg += int(row['Grid carbon intensity (gCO2eq / kWh)'])
            nb = nb + 1
        print("avg = {}".format(avg/nb))

if __name__ == '__main__':
    main()
