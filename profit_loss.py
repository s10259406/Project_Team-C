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

profit_deficit = 0   
day_profit_deficit = 0
max_profit_surplus = 0
day_profit_surplus = 0

 # Use a loop to iterate over the profitnloss list (*the start in range is default to 0)
for data in range(len(profitnloss)):

    # get the current day and net profit
    day = profitnloss[data][0]
    net_profit = profitnloss[data][1]

    # if it is the 1st day, there is no previous day to compare with
    if data == 0: # day = [0][0] = day 1 
      # thus the difference is zero
      difference = 0
    else:
      # get the previous day's net profit
      previous_net_profit = profitnloss[data-1][1]
      # calculate the difference by subtracting the previous net profit from the current net profit
      difference = net_profit - previous_net_profit

      # check if the difference is negative, mean there is a deficit
      if difference < 0:
        profit_deficit = difference * -1
        day_profit_deficit = day 
        print(f'[PROFIT DEFICIT] Day: {day_profit_deficit}, Amount: USD{profit_deficit}')
      
      # check if the difference is positive, mean there is a surplus
      elif difference > 0:
        profit_deficit = difference
        day_profit_deficit = day 
        print(f'[PROFIT SURPLUS] Day: {day_profit_deficit}, Amount: USD{profit_deficit}')

      # compare the difference with the max_profit_deficit
      if difference > 0:
        if difference > max_profit_surplus:
          max_profit_surplus = difference
          day_profit_surplus = day     
print(f'[HIGHEST PROFIT SURPLUS] Day: {day_profit_surplus}, Amount: USD{max_profit_surplus}')
