# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.
# x = 67
# tens_digit = x//10
# ones_digit = x%10
print('Type any number here: ')
integer = input()
while not (integer.isdigit()):
    print('Only numbers are allowed!')
    print('Type any number here: ')
    integer = input()

ones = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
tens = { '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
decades={'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen', '5': 'fifteen', '6': 'sixteen', '7': 'seventeen', '8': 'eighteem'}
hundreds = {'0': '1': 'one hundred', '2': 'two hundred', '3': 'three hundred', '4': 'four hundred', '5': 'five hundred', '6': 'six hundred', '7': 'seven hundred', '8': 'eight hundred', '9': 'nine hundred'}
comma_word = {'3': 'thousand', '6': , 'million', '9': 'billion'}




word = ''
integer_side = integer 
int_length = len(integer)
integer_change = len(integer)
change = 3 
while integer_change > 0:
    if integer == '0':
        word = 'zero'
        break
    if integer_side[integer_change -2] == '1':
        for digit in tens:
            if integer_side[integer_change - 1] == digit_1:
                word = ones[digit] + word 
    else:
        for digit_1 in ones:
            if integer_side[integer_change -1] == digit_1:
                word = ones[digit_1] + word 
            for digit_2 in decades:
                if integer_side[integer_change -2] == digit_2:
                    word = decades[digits_2] + word
    if integer_change > 2:
        for digit_3 in hundreds: 
            if integer_side[integer_change -3] == digit_3: 
                word = hundreds[digit_3] + word 
    if integer_change > 3: 
        word = comma_word[str(change)] + word
    change = change + 3
    integer_change = integer_change - 3
    print(word)









num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def number(Number):

    if (Number > 1) or (Number < 19):
        return (num2words1[Number])
    elif (Number > 20) or (Number < 99):
        return (num2words2[Number])
    else:
        print("Number Out Of Range")
        main()

def main():
    num = eval(input("Please enter a number between 0 and 99: "))
    number(num)
main()