from pathlib import Path
import csv
fp =Path.home()/"p4b igp"/"Project_Team-C"/"csv_reports"/"Cash_on_Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    cashonhands = []
    for row in reader:
        cashonhands.append([row[0],row[1]])
# print(cashonhands)

prev_coh = 0
highest_surplus = 0
for item in cashonhands:
    coh = int(item[1])
    if coh < prev_coh:
        surplus = prev_coh - coh
        print(f'surplus {item[0]} {surplus}')
        if surplus > highest_surplus:
            highest_day = f"{item[0]}"
            highest_surplus = surplus
    prev_coh = coh
print(f"highest surplus {highest_day} {highest_surplus}")

for item in cashonhands:
    coh = int(item[1])
    if coh > prev_coh:
        deficit = coh - prev_coh
        print(f'deficit {item[0]} {deficit}')
    prev_coh = coh

