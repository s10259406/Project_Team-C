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

def coh_function (option):

    '''
    - The function will return the cash surplus and cash deficit
    - Required parameter: option 
    '''

    # initialize variables to store the value
    prev_coh = 0
    highest_surplus = 0
    highest_day = 0

    # initialize an empty string to store the results
    results = ''

    if option == 'Surplus':
        # use for loop to iterate over the data in cashonhands list
        for item in cashonhands:
            coh = int(item[1])
            # checking whether there is a surplus and calculating it
            if coh < prev_coh:
                surplus = prev_coh - coh
                results += f'[CASH SURPLUS] DAY: {item[0]}, AMOUNT: USD{surplus}\n'
                # finding out the highest surplus among all the other surpluses
                if surplus > highest_surplus:
                    highest_day = f"{item[0]}"
                    highest_surplus = surplus
            prev_coh = coh
        results += f"[HIGHEST CASH SURPLUS] DAY: {highest_day}, AMOUNT: USD{highest_surplus}\n"
        return results

    elif option =='Deficit':
        for item in cashonhands:
            coh = int(item[1])
            # checking whether there is a deficit and calculating it
            if coh > prev_coh:
                deficit = coh - prev_coh
                results += f'[CASH DEFICIT] DAY: {item[0]}, AMOUNT: USD{deficit}\n'
            prev_coh = coh
    return results

# print(coh_function('Surplus'))
# print(coh_function('Deficit'))