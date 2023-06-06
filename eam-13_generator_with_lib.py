from barcode import EAN13
from barcode.writer import ImageWriter

def count_checkdigit(number):
    ListOfNumbers = [int(i) for i in digits]
    sum_even,sum_odd = 0,0

    for i in range(len(ListOfNumbers)):
        if i%2:
            sum_even += ListOfNumbers[i]
        else:
            sum_odd += ListOfNumbers[i]

    sum = 3 * sum_even + sum_odd
    checkDigit = None

    if sum%10 == 0:
        checkDigit = 0
    else:
        checkDigit = 10 - sum%10

    return checkDigit

digits = '590488380299'


checkDigit = count_checkdigit(digits)

FullNumber = digits + str(checkDigit)


my_barcode = EAN13(FullNumber, writer=ImageWriter())

my_barcode.save("kod_kreskowy")