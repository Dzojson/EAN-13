import cv2 as cv
import numpy as np

#tablica kodowania pierwszej grupy
Letters = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']

#słownik z bitami w zależnosći od kodowania 
Charracters = {"L": ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011'],
"G": ['0100111', '0110011', '0011011', '0100001', '0011101', '0111001', '0000101', '0010001', '0001001', '0010111'], 
"R": ['1110010', '1100110', '1101100', '1000010', '1011100', '1001110', '1010000', '1000100', '1001000', '1110100']}

#funkcaja licząca liczbe kontrolną
def count_checkdigit(number):
    ListOfNumbers = [int(i) for i in number]
    sum_even,sum_odd = 0,0

    for i in range(len(ListOfNumbers)):
        #zliczanie sumy liczb na miejscach parzystych
        if i%2:
            sum_even += ListOfNumbers[i]
        #zliczanie sumy liczb na miejscach nie parzysty 
        else:
            sum_odd += ListOfNumbers[i]

    #suma liczb 
    sum = 3 * sum_even + sum_odd
    checkDigit = None

    #obliczenie liczby kontrolnej
    if sum%10 == 0:
        checkDigit = 0
    else:
        checkDigit = 10 - sum%10

    return checkDigit

# funkcja sprawdzający typ kodowania
def type_of_coding(number):
    code = Letters[int(number[0])]
    return code

def Dec_to_Bits(number, code):
    barcodeInBits = ''
    #tworzenie kodu bitowego za pomoca kodu LGR
    for i in range(len(number)):
        if int(i) > 0 and int(i) <= 6:
            barcodeInBits += Charracters[code[int(i)-1]][int(number[int(i)])]
            #stworzenie kresek odzielających
            if int(i) == 6:
                barcodeInBits += '01010'  
        elif int(i) > 6:
            barcodeInBits += Charracters['R'][int(number[int(i)])]

#dodanie marginesu z lewej i prawej strony
    barcodeInBits = '101' + barcodeInBits + '101'
    return barcodeInBits

#wprowadenie 12 cyfr
numberOfBarcode = '590008900449'

checkDigit = count_checkdigit(numberOfBarcode)
print(checkDigit)

FullNumber = numberOfBarcode + str(checkDigit)

code = type_of_coding(numberOfBarcode)

barcodeInBits = Dec_to_Bits(FullNumber, code)


Img = np.zeros((500, 700, 3),dtype=np.uint8)
Img.fill(255)
start_point = [100, 100]
end_point = [100, 450]

#tworzenie kodu kreskowego 
for i in barcodeInBits:
    if int(i) == 1:
        Img = cv.rectangle(Img , start_point, end_point, (0,0,0), 5)

    elif int(i) == 0:
        Img = cv.rectangle(Img , start_point, end_point, (255,255,255), 5)


    start_point[0] += 5
    end_point[0] += 5

cv.imshow("Drawing_Line", Img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("kod_kreskowy.jpg", Img)
