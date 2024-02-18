# This program prompts for an arabic number between 1 and 99 and returns its roman numeral
# equivalent. It implements the rules that structure roman numerals provided at the end of
# this file. There are two functions -- one to convert single digit numbers, the other to 
# convert double-digit numbers (the length of the number is determined while it is a string).  
# The double digit conversion function separates the number into tens and ones. E.g., the number 
# 52 has five tens and two ones. After the double digit function, convert_tens(), converts the 
# tens, if there are ones, it calls the single digit conversion function, convert_ones(), 
# it concatenates the two values and returns the resulting roman numeral.

symbol_I = 'I' #1
symbol_V = 'V' #5
symbol_X = 'X' #10
symbol_L = 'L' #50
symbol_C = 'C' #100
symbol_D = 'D' #500
symbol_M = 'M' #1000
roman_numeral = ''

def convert_ones(number):
    i = 0
    symbol_string = ''
    ones = int(number)
    if ones <= 3:
        for _ in range(ones):
            symbol_string = symbol_string + symbol_I
    if ones == 4:
        symbol_string = symbol_string + symbol_I + symbol_V
    if ones >= 5:
        symbol_string = symbol_string + symbol_V
        if ones >= 6 and ones <= 8:
                i = ones - 5
                for _ in range(i):
                    symbol_string = symbol_string + symbol_I
    if ones == 9:
        symbol_string = symbol_I + symbol_X
    return(symbol_string)

def convert_tens(number):
    i = 0
    symbol_string = ''
    ones_symbol_string = ''
    tens = number//10
    print('tens = ', tens)
    tens_remainder = number%10
    print('ones = ', tens_remainder)
    if tens >= 2 and tens < 3:
        for _ in range(tens):
            symbol_string = symbol_string + symbol_X
    if tens >= 3 and tens < 4:
        for _ in range(tens):
            symbol_string = symbol_string + symbol_X
    if tens == 4:
        symbol_string = symbol_string + symbol_X + symbol_L
    if tens >= 5:
        symbol_string = symbol_L
        if tens >= 6 and tens <= 8:
                i = tens - 5
                for _ in range(i):
                    symbol_string = symbol_string + symbol_X
    if tens == 9:
        symbol_string = symbol_X + symbol_C
    if tens_remainder > 0:
        ones_symbol_string = convert_ones(tens_remainder)
    symbol_string = symbol_string + ones_symbol_string
    return(symbol_string)

input_number = input('Enter an arabic number between 1 and 99: ')
number = int(input_number)
print('converting:', number)
digits = len(input_number)
print('digits = ', digits)

if digits == 1:
    roman_numeral = convert_ones(number)
    print(f'The roman numeral for {number} is: {roman_numeral}')

if digits == 2:
    roman_numeral = convert_tens(number)
    print(f'The roman numeral for {number} is: {roman_numeral}')



# Symbols
# I: 1
# V: 5
# X: 10
# L: 50
# C: 100
# D: 500
# M: 1000

# Rules
# Combining Symbols: Roman numerals are formed by combining symbols to represent numbers. 
# The symbols are combined from left to right, with larger symbols placed before smaller symbols 
# to indicate addition.

# Repeating Symbols: A symbol may be repeated up to three times in succession to represent 
# addition of the value. However, no more than three identical symbols are used in a row. For 
# example, III represents 3 (1 + 1 + 1), but four "I"s in a row (IIII) are not used; instead, 
# IV represents 4 (5 - 1).

# Subtractive Notation: Smaller symbols placed before larger symbols indicate subtraction. 
# Subtraction is used in the following cases:

# Examples
# "IV" represents 4 (5 - 1)
# "IX" represents 9 (10 - 1)
# "XL" represents 40 (50 - 10)
# "XC" represents 90 (100 - 10)
# "CD" represents 400 (500 - 100)
# "CM" represents 900 (1000 - 100)
# Ordering: Symbols are arranged from left to right in descending order of value. However, certain exceptions are made to the order to follow the subtraction rule. For example, "IV" and "IX" are used instead of "IIII" and "VIIII" to represent 4 and 9, respectively.

# Examples
# "XLIV" represents 44 (50 - 10 + 1 + 1 + 1)
# "XCIX" represents 99 (100 - 10 + 10 - 1)
# "CDXLV" represents 445 (500 - 100 + 50 - 10 + 5)
