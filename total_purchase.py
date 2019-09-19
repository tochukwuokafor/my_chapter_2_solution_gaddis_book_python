SALES_TAX = 0.07
ITEMS = 5
total = 0
for item in range(5):
    print('Enter the price of item #', item + 1, ' : $', sep='', end = '')
    sub = float(input())
    total += sub

print('The subtotal of the sale is ${:.2f}'.format(total))
tax = total * SALES_TAX
print('The amount of sales tax is ${:.2f}'.format(tax))
main_total = tax + total
print('The total is ${:.2f}'.format(main_total))