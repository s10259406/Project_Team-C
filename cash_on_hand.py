from pathlib import Path
import csv
fp =Path.home()/"p4b igp"/"Project_Team-C"/"csv_reports"/"Cash_on_Hand.csv"
# print(fp.exists())
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    cashonhands = []
    for row in reader:
        cashonhands.append([row[0],row[1]])
# print(cashonhands)
