# This a code which calculates the profit and other data regarding the sales of a company throughout the year

import statistics
import numpy as np
# data for each month
revenue = [14574.49, 7606.46, 8611.41, 9175.41,
           8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72,
            8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

counter = 0
profitEachMonth = []
while counter < 12:
    profitEachMonth.append(revenue[counter] - expenses[counter])
    counter = counter + 1


months = ["January", 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
meanProfitForYear = float(statistics.mean(profitEachMonth))
# print(profitEachMonth)


def base_profit(month):
    print("Profit for the month", months[month], 'is', profitEachMonth[month])


def profit_after_tax(month):
    print("Profit after tax of 30% for the month", months[month], 'is',
          (profitEachMonth[month]*0.7))


def profit_margin(month):
    print('Profit margin for the month', months[month], 'is',
          ((revenue[month]-expenses[month])/revenue[month])*100, '%')


def worst_month():
    worstMonthIndex = []
    worstMonths = []
    for i in range(0, 12):
        if profitEachMonth[i] < meanProfitForYear:
            worstMonthIndex.append(i)
    print('The following were the bad months ('
          'i.e Months which had profit less than the average mean profit for the year)')
    for count in range(0, len(worstMonthIndex)):
        print(months[worstMonthIndex[count]])
        worstMonths.append(profitEachMonth[worstMonthIndex[count]])
    print('The worst month of the year was : ', months[profitEachMonth.index(min(worstMonths))])


def best_month():
    bestMonthIndex = []
    bestMonths = []
    for i in range(0, 12):
        if profitEachMonth[i] > meanProfitForYear:
            bestMonthIndex.append(i)
    print('The following were the good months '
          '(i.e Months which had profit more than the average mean profit for the year)')
    for count in range(0, len(bestMonthIndex)):
        print(months[bestMonthIndex[count]])
        bestMonths.append(profitEachMonth[bestMonthIndex[count]])
    print('The best month of the year was : ', months[profitEachMonth.index(max(bestMonths))])


# dictionary of functions for the program


base_functions = {0: base_profit, 1: profit_after_tax, 2: profit_margin}
monthNumber = 0
while monthNumber < 12:
    print('The Following is the information for the month', months[monthNumber], '\n')
    for count_2 in range(0, 3):
        base_functions[count_2](monthNumber)
    monthNumber = monthNumber + 1
    print('-----------------*---------------------*--------------------*------------------------')  # delimiter


best_month()
