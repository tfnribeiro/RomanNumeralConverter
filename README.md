# RomanNumeralConverter
 Simple python script to convert Numerals to Roman numerals and vice versa.

# Usage
 1. Roman to Numeral: rn to convert from Roman Numeral to Numeral, you may pass more than 1 number.
 ```
    Ex:
    python RomanConverter.py rn X XX XXX CXII
    X  :  10
    XX  :  20
    XXX  :  30
    CXII  :  112
 ```
 
 2. Numeral to Roman: nr to convert from Numeral to Roman Numeral, you may again pass more than 1 number.
 ```
    Ex:
    python RomanConverter.py nr 123 222 303
    123  :  CXXIII
    222  :  CCXXII
    303  :  CCCIII
 ```

# Note
 You can only convert from 1 - 3999.
 To convert from Roman to Numeral the algorithm generates a pickle file with all numbers from 1 - 3999 and will return this mapping. This will have the name numToRomanDict.pkl 
