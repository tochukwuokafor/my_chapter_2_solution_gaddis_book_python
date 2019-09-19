SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75
COOKIE = 48

number_cookie = int(input("Enter the number of cookies you'd like to make: "))
sugar = number_cookie * SUGAR/COOKIE
butter = number_cookie * BUTTER/COOKIE
flour = number_cookie * FLOUR/COOKIE
print("You'll need {:.2f} cups of sugar, {:.2f} cups of butter, and {:.2f} cups of flour".format(sugar, butter, flour))