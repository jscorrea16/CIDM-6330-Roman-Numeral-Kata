def arabic_to_roman(x):


roman = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
numbers = {1, 5, 10, 50, 100, 500, 1000}
i = 7
roman_numeral = ''
while x != 0:
    if numbers[i] <= x:
        roman_numeral += roman[i]
        x = x - numbers[i]
    else:
        i -= 1
return roman_numeral
