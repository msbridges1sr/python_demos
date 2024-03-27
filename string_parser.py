# This program prompts for a string and returns its length and a count of spaces and non-spaces present.
# The function parse_string() iterates the string using enumerate() to obtain position indexes and tests for a space.
# When a space is found the spaces counter is incremented, otherwise the non-spaces counter is incremented.
# It returns a tuple with the two counts and prints the result.   

# Function to parse an input string and count spaces and non-spaces
def parse_string(string):
    """
    Count the number of spaces and non-spaces in the input string.

    Args:
        string (str): The input string to parse.

    Returns:
        tuple: A tuple containing the count of spaces and non-spaces.
    """
    count_non_space = 0
    count_space = 0
    for index, letter in enumerate(string):
        #print(f'index {index}, letter {letter}')
        if (letter == ' '):
            count_space += 1
        else:
            count_non_space +=1
    return count_space, count_non_space 

# Prompt for a string and measure its length
input_string = input('Enter a string: ')
length_input_string = len(input_string)

# Pass the input string to the parse_string() function and print the result
cs, cns = parse_string(input_string)
print(f'The input string entered is {length_input_string} characters long and has '
      f'{cs} spaces and {cns} non-spaces.')
