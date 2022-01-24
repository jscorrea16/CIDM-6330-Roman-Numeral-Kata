num_dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50,
           'X': 10, 'V': 5, 'IV': 4, 'III': 3, 'II': 2, 'I': 1}


def roman2arabic(numeral):
    answer = 0
    n = len(numeral)
    for (idx, c) in enumerate(numeral):
        if idx < n-1 and num_dic[c] < num_dic[numeral[idx + 1]]:
            answer = answer - num_dic[c]
        else:
            answer = answer + num_dic[c]
            return answer


again = 'y'

while again == 'y':
    numeral = input("Please enter Roman Numeral to convert: ")
    numeral = numeral.upper()
    print(roman2arabic(numeral))
    again = input("Would you like to convert another Roman Numeral? <y/n>")
