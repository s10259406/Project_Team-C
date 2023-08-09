from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and net profit
    profitnloss = []
    # append day and net profit into profitnloss list
    for row in reader:
        net_profit = float(row[4])
        # get the day and net profit for each record and append the profitnloss list
        profitnloss.append([row[0],net_profit])
# print(profitnloss)
