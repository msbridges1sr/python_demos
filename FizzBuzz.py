# FizzBuzz program. Prompts for an integer and performs FizzBuzz logic.

import time
import os
import traceback
import logging

logger = logging.getLogger(__name__)
   

def convert_to_integer_or_fail(input_string):
    """
    Converts a string to an integer or raises a ValueError on failure.

        Args:
            input_string (str): The string to convert.

        Returns:
            int: The integer value converted from the input string.
            
        Raises: 
            ValueError: If conversion fails, typically due to the input string
                not representing a valid integer.
    """

    # Convert received input_string into integer and return
    logger.info(f"Attempting to convert input string: {input_string}")
    try:
        return int(input_string)
    except ValueError as e:
        # Log the exception with the full stacktrace
        logger.error("Conversion failed for input:", exc_info=True)
        
        # Print the stacktrace to the screen
        print("Conversion failed. Stacktrace:")
        traceback.print_exc()
        
        # Raise a ValueError with an informative message
        raise ValueError(f"Please enter a positive or negative integer for FizzBuzz")

def FizzBuzz(upper_limit):
        """
        Prints the FizzBuzz sequence up to a given 
        upper_limit integer.

        Args:
            upper_limit: An integer representing the upper
            limit of the FizzBuzz sequence (exclusive). 
            Numbers will be printed from 1 to upper_limit-1.

        Prints:
            FizzBuzz sequences according to the following
            rules:
                - If a number is divisible by 3, print
                 "Fizz".
                - If a number is divisible by 5, print
                  "Buzz".
                - If a number is divisible by both 3 and
                  5, print "FizzBuzz".
                - Otherwise, print the number itself.
        """

        # Set for loop parameters based on positive or negative upper_limit entry 
        if upper_limit < 0:
            start = upper_limit
            end = 1 # Include 1 to handle 0 as well
            step = 1  # Increase instead of decrease for negative range
        else:
            start = 1
            end = upper_limit + 1 #Include upper_limit for positive range
            step = 1

        # Perform FizzBuzz logic on range of numbers defined by 'upper_limit' entry
        for number in range(start, end, step):
            if (number % 3) == 0 and (number % 5) == 0:
                print('FizzBuzz')
                continue
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)

def main():
    start_time = time.time()
    end_time = 0
    duration_formatted = ""
    """ Configure logging and clear screen"""
    logging.basicConfig(filename = 'FizzBuzz.log', level=logging.INFO, \
        format = '%(asctime)s - %(levelname)s - %(message)s', \
        datefmt = '%Y-%m-%d %H:%M:%S')
    logger.info('Started')
    os.system('cls')

    print(f"Enter a positive or negative number. FizzBuzz will count up to that\n"
        "number evaluating each number along the way. If it is divisible\n"
        "by 3, it will print Buzz. If divisible by 5 Buzz.\n"
        "If divisible by 3 and 5 FizzBuzz. Otherwise it will display the number.\n"
        "\n")
    
    # Start game loop and get user entry (positive or negative number) 
    keep_playing = True
    
    while keep_playing:
        input_string = input("Enter your number: ")
        print("Checking: ", input_string)
        logger.info(f'User entered: {input_string}, starting FizzBuzz')
        
        # Convert user entry into an integer and pass it to FizzBuzz
        try:
            result = convert_to_integer_or_fail(input_string)
            
            # Measure duration of FizzBuzz
            start_time = time.time()
            FizzBuzz(result)
            end_time = time.time()

        except ValueError as e:
            print(f"Main: ValueError e: {e}")
            logger.error(f'Error: {e}')

        # Prompt user to play again or quit
        play_again = input("Would you like to play again? Enter 'y' for yes, any other key for no: ")
        if play_again == 'y':
            continue
        else:
             print('Bye')
             keep_playing = False
    logger.info('Finished')

if __name__ == '__main__':
    main()
