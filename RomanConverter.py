import sys
from random import randint
import time
import pickle
import os.path
from os import path

def convertToRoman(num):
    roman_num = {
        1   : "I", 
        5   : "V",
        10  : "X",
        50  : "L", 
        100 : "C", 
        500 : "D", 
        1000 : "M",
    }
    # The system can be looked at
    # with 3 cases for each of the 
    # order of greatness.
    # We right higher magnitude first
    # 1. The number matches one of the dic
    # -> add it to the return result
    # 2. The number is the one before a major 
    # number (4 to 5, 9 to 10) -> add the 
    # singular unit behind the next number
    # 3. The number is not adjacent to a higher
    # unit -> We add the number of units to the 
    # closest lowest unit 
    number_to_string = str(num)
    roman_numeral = ""
    for i in range(len(number_to_string)):
        magnitude = 10**(len(number_to_string) - 1 - i)
        number = int(number_to_string[i]) * magnitude
        if number == 0:
            continue
        # Case 1.
        if number in roman_num:
            roman_numeral += roman_num[number]
            continue
        # Case 2.
        case2_used = False
        for n in list(roman_num):
            if number == n - magnitude:
                roman_numeral += roman_num[magnitude] + roman_num[n]
                case2_used = True
        # Case 3.
        if(not case2_used):       
            if number < 5 * magnitude:
                temp_num = 0
                while(temp_num < number):
                    temp_num += magnitude
                    roman_numeral += roman_num[magnitude]
            else:
                temp_num = 5 * magnitude
                roman_numeral += roman_num[temp_num]
                while(temp_num < number):
                    temp_num += magnitude
                    roman_numeral += roman_num[magnitude]
    return roman_numeral

def test():
    assert convertToRoman(1412) == "MCDXII",  "1412 should be 'MCDXII'"
    assert convertToRoman(3299) == "MMMCCXCIX", "3299 should be 'MMMCCXCIX'"
    assert convertToRoman(622) == "DCXXII", "622 should be 'DCXXII'"
    assert convertToRoman(3082) == "MMMLXXXII", "3082 should be 'MMMLXXXII'"
    assert convertToRoman(1254) == "MCCLIV", "3082 should be 'MCCLIV'"
    assert convertToRoman(1) == "I", "1 should be 'I'"
    assert convertToRoman(2) == "II", "1 should be 'II'"
    assert convertToRoman(3) == "III", "1 should be 'III'"
    assert convertToRoman(4) == "IV", "1 should be 'IV'"
    assert convertToRoman(5) == "V", "1 should be 'V'"
    assert convertToRoman(43) == "XLIII", "43 should be 'XLIII'"
    print("Test passed!")
def generateMapping(n):
    t = time.time()
    dictRoman = {}
    for i in range(1,n):
        dictRoman[convertToRoman(i)] = i
    f = open("numToRomanDict.pkl", "wb")
    pickle.dump(dictRoman,f)
    f.close()
    return dictRoman
def main(argv):
    if(path.exists(".\\numToRomanDict.pkl")):
        dictRoman = pickle.load(open("numToRomanDict.pkl", "rb"))
    else:
        dictRoman = generateMapping(3999)
        print("Generated Mapped File!")
    if not argv or argv[0] == "help":
        print("use rn - to convert roman to numeral | use nr - to convert numeral to roman")
        print("Format: rn XX X IV | nr 230 123 111")
    elif argv[0] == "nr":
        for i in range(1,len(argv)):
            try:
                num = int(argv[i])
                print(num, " : ", convertToRoman(num))
            except ValueError:
                print("Argument was not a valid int.")
    elif argv[0] == "rn":
        for i in range(1,len(argv)):
            try:
                print(argv[i], " : ", dictRoman[argv[i]])
            except ValueError:
                print("The number was not found in the mapping. Remember only Natural Numbers until 3300.")
    else:
        print("use rn - to convert roman to numeral | use nr - to convert numeral to roman")
        print("The limit of conversion is 3300.")
        
if __name__ == "__main__":
    main(sys.argv[1:])