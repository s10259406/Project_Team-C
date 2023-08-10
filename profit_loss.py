from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"Profit_and_Loss.csv"

# create 'reader' object and print line if file path exists
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and net profit
    profitnloss = []
    # append day and net profit into profitnloss list
    for row in reader:
        net_profit = int(row[4])
        # get the day and net profit for each record and append the profitnloss list
        profitnloss.append([row[0],net_profit])
# print(profitnloss)

def profitloss_function (option):
   
  '''
  - The function will return the profit surplus and profit deficit
  - Required parameter: option
  '''

  # initialize variables to store the data
  previous_net_profit = 0
  max_profit_surplus = 0
  day_profit_surplus = 0

  # initialize an empty string to store the results
  results = ''

  if option == 'Surplus':
      # use a for loop to iterate over the data in profitnloss list
      for data in profitnloss:
        day = data[0]
        net_profit = int(data[1])

        # checking if the net profit on the current day is higher than the previous day
        if net_profit > previous_net_profit:
           # calculate the difference by subtracting the previous net profit from the current net profit
           difference = net_profit - previous_net_profit
           results += f'[NET PROFIT SURPLUS] DAY:{day}, AMOUNT: USD{difference}\n'
           # finding the highest profit surplus among all the profit surpluses
           if difference > max_profit_surplus:
              day_profit_surplus = data[0]
              max_profit_surplus = difference
        previous_net_profit = net_profit
      results += f'[HIGHEST PROFIT SURPLUS] DAY:{day_profit_surplus}, AMOUNT: USD{max_profit_surplus}\n'
      return results


  elif option == 'Deficit':
     #  use a for loop to iterate over the data in profitnloss list
     for data in profitnloss:
        day = data[0]
        net_profit = int(data[1])

        # checking if the net profit on the current day is lower than the previous day
        if net_profit < previous_net_profit:
           # calculate the difference by subtracting the previous net profit from the current net profit
           difference = (net_profit - previous_net_profit) * -1
           results += f'[PROFIT DEFICIT] DAY:{day}, AMOUNT: USD{difference}\n'
        previous_net_profit = net_profit
  return results

# print(profitloss_function('Surplus'))
# print(profitloss_function('Deficit'))

           