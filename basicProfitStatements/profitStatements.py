# This a code which calculates the profit and other data regarding the sales of a company throughout the year

import statistics
import numpy as np
# data for each month
revenue = [14574.49, 7606.46, 8611.41, 9175.41,
           8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72,
            8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

counter = 0
r = np.array(revenue)
e = np.array(expenses)


profitEachMonth = []
profitEachMonth = r-e


months = ["January", 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

meanProfitForYear = statistics.mean(profitEachMonth)

profitAfterTax = []
i = 0
while i < len(r):
    profitAfterTax.append((profitEachMonth[i]-(profitEachMonth[i]*0.3)))


# print(profitEachMonth)


def base_profit(month):
    print("Profit for the month", months[month], 'is', profitEachMonth[month])


def profit_after_tax(month):
    print("Profit after tax of 30% for the month", months[month], 'is',
          (profitEachMonth[month]-(profitEachMonth[month]*0.3)))


def profit_margin(month):
    print('Profit margin for the month', months[month], 'is',
          ((revenue[month]-expenses[month])/revenue[month])*100, '%')


base_functions = {0: base_profit, 1: profit_after_tax, 2: profit_margin}