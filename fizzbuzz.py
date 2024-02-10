#FizzBuzz--this program prompts for an integer, iterates from one through the 
#inteteger received testing each number's mod result for 3 and 5. If both 3 and 5
#have mod value zero, it prints 'FizzBuzz'. If only the mod 3 value is 0, it prints
#'Fizz'. If only the mod 5 value is 0, it prints 'Buzz'. 

import os
os.system('cls')
target_str = input("Enter a target number: ")
target = int(target_str)
target += 1
for number in range(1, target, 1):
    if ((number % 3) == 0) and ((number % 5) == 0):
        print('FizzBuzz')
        continue
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


