# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

def input():
    print("Enter the card number: ")
    firsthalf= list()
    sechalf= list()
    for i in range (1,17):
        x = int(input())
        if i<9:
            firsthalf.append(x)
        else: 
            sechalf.append(x)

def process(): 
    sum1=int(0)
    sum2=int(0)
    for i in firsthalf: 
        sum1=sum1+i 
    for i in sechalf: 
        sum2=sum2+i
    print(sum1, sum2)