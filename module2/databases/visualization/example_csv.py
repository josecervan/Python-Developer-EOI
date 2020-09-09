import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data\sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    heads = [(index, column_header) for index, column_header in enumerate(header_row)]
    print(heads)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

    