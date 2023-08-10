from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"Overheads.csv"

# create 'reader' object and print line if file path exists
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the overheads
    overheads = []
    # append the category and overheads into overheads list
    for row in reader:
        # get the category and overheads for each record and append the overheads list
        overheads.append([row[0],(row[1])])
# print(overheads)

def overheads_function(option):

    '''
    - The function will return the highest overhead
    - Required parameter: option
    '''

    # initialize variable to store the highest overhead value and category
    highest_overhead = 0
    highest_category = ''
    
    if option == 'max_ovh':
        # use for loop to iterate over the data in overheads list
        for cat, ovh in overheads:
            # convert str to float
            ovh = float(ovh)
            # compare the current overheads value with the highest overheads value
            if ovh > highest_overhead:
                # if the current overhead value is larger, it will be updated until finding the highest value and category
                highest_category = cat
                highest_overhead = ovh
        return(f'[HIGHEST OVERHEAD] {highest_category.upper()}: {highest_overhead}%\n')

# print(overheads_function('max_ovh'))
