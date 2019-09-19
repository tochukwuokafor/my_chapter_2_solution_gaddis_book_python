sales = float(input('Enter the projected anount of sales: '))
PROFIT = 0.23
total_profit = PROFIT * sales
print('The profit that will be made from $', sales, ' is $', '{:.2f}'.format(total_profit), sep = '')