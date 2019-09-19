p = float(input('Enter the amount of deposit originally deposited into the account: '))
r = float(input('Enter the annual interest paid by the account: '))
rate = r / 100
n = int(input('Enter the number of times per year that the interest is compounded: '))
comp = n / 12
t = int(input('Enter the number of years the account will be left to earn interest: '))
amount = p * ((1 + (r / n)) ** (comp * t))
print('The amount of money that will be in the account after ', t, ' years is ${:.2f}'.format(amount), sep = '')