purchase = float(input('Enter the amount of purchase: $'))
PERCENT = 0.05
percent_purchase = PERCENT * purchase
total_purchase = purchase + percent_purchase
instalment = int(input('Enter the number of payment instalments: '))
payment_instalment = total_purchase / instalment
print('The total amount of the purchase is ${:.2f}'.format(total_purchase))
print('Each instalment will cost ${:.2f}'.format(payment_instalment))