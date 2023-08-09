from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
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
    # checking whether there is a surplus and calculating it
    if coh < prev_coh:
        surplus = prev_coh - coh
        print(f'[CASH SURPLUS] DAY: {item[0]}, AMOUNT: USD{surplus}')
        # finding out highest surplus among all the other surpluses
        if surplus > highest_surplus:
            highest_day = f"{item[0]}"
            highest_surplus = surplus
    prev_coh = coh
print(f"[HIGHEST CASH SURPLUS] DAY: {highest_day}, AMOUNT: USD{highest_surplus}")


for item in cashonhands:
    coh = int(item[1])
    # checking whether there is a deficit and calculating it
    if coh > prev_coh:
        deficit = coh - prev_coh
        print(f'[CASH DEFICIT] DAY: {item[0]}, AMOUNT: USD{deficit}')
    prev_coh = coh