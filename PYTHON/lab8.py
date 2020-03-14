
x = float(input('Please enter an amount between 0-99:'))
print(x//.25, "quarters")
x = x%25
print(x//.10, "dimes")
x = x%10
print(x//.5, "nickles")
x = x%.05
print(x//.01, "pennies")
x = x%.01/100

q = .25
d = .10
n = .05
p = .01




# Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136
# Have the user enter a dollar amount (1.36), convert this to the total in pennies.