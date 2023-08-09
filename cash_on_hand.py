from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
# print(fp.exists())
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    cashonhands = []
    for row in reader:
        cashonhands.append([row[0],row[1]])
# print(cashonhands)

prev_coh = 0
for item in cashonhands:
    coh = int(item[1])
    if coh < prev_coh:
        difference = prev_coh - coh
        print(f'surplus{item[0]} {difference}')
    prev_coh = coh

for item in cashonhands:
    coh = int(item[1])
    if coh > prev_coh:
        difference = coh - prev_coh
        print(f'deficit {item[0]} {difference}')
    prev_coh = coh

