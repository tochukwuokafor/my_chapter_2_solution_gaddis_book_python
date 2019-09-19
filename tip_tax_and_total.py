charge = float(input('Enter the charge for the food: $'))
TIP = 0.18
amount_tip = charge * TIP
print('The amount of tip is ${:.2f}'.format(amount_tip))
TAX = 0.07
sales_tax = charge * TAX
print('The amount of sales tax is ${:.2f}'.format(sales_tax))
total = charge + amount_tip + sales_tax
print('The total cost is ${:.2f}'.format(total))