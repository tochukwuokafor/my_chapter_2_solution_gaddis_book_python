r = float(input('Enter the length of the row, in feet: '))
e = float(input('Enter the amount of space used by the end-post assembly, in feet: '))
s = float(input('Enter the amount of space between the vines, in feet: '))
v = (r - (2 * e)) / s
print('The number of grapevines that will feet in the row is ', v)