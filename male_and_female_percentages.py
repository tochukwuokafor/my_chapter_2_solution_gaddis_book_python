male = int(input('Enter the number of males in the class: '))
female = int(input('Enter the number of females in the class: '))
total = male + female
male_percent = (male / total) * 100
female_percent = (female / total) * 100
print('The percentage of males in the class is {:.2f}%'.format(male_percent))
print('The percentage of females in the class is {:.2f}%'.format(female_percent))