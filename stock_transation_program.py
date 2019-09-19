SHARES_BOUGHT = 2000
COST_BOUGHT = 40
COMMISSION = 0.03
commission_on_buy = COMMISSION * (COST_BOUGHT * SHARES_BOUGHT)
SHARES_SOLD = 2000
COST_SOLD = 42.75
commission_on_sale = COMMISSION * (SHARES_SOLD * COST_SOLD)
paid = COST_BOUGHT * SHARES_BOUGHT
print('The amount Joe paid for the stock is $', paid)
print('The amount of commission Joe paid his broker when he bought the stock is $', commission_on_buy)
sold = SHARES_SOLD * COST_SOLD
print('The amount Joe sold the stock is $', sold)
print('The amount of commission Joe paid his broker when he sold the stock is $', commission_on_sale)
amount_left = (sold - commission_on_sale) - (paid + commission_on_buy)
print('Joe has $', amount_left, ' left.', sep = '')