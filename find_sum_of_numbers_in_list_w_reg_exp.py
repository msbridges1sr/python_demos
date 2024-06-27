from typing import List
import re
    
def pluck_floats(case_str: str) -> List[str]:
    """
    This function receives a string and applies a regular expression to 
    it which matchs all floating point numbers in the format '<digit>.<digit>'.

    Args:
        case_str (string): the string to search for floating point numbers.

    Returns:
        matches (list): the list of floating point numbers found in case_str.
    """

    pattern = r"\d\.\d"
    matches = re.findall(pattern, case_str)
    return matches


def pluck_digits(case_str: str) -> List[str]:
    """
    This function receives a string and applies a regular expression
    to it which matchs digits not part of a floating point number in the 
    format '<digit>'.

    Args:
        case_str (string): the string to search for digits.

    Returns:
        matches (list): the list of digits found in case_str.
    """

    pattern = r'(?<!\.)\b\d\b(?!\.)|(?<!\.)\d(?!\.)'
    matches = re.findall(pattern, case_str)
    return matches


def get_sum(numbers_list: List[float]) -> float:
    """
    This function receives a list of numbers and returns their sum.
    
    Args:
        numbers_list (list): the list of numbers to add together.
    
    Returns:
        sum (int): the sum of all numbers in the numbers_list arg.
    """

    return sum(float(num) for num in numbers_list)
        
def main():
    cases_list = [
        "Some text with numbers like 4,5 and 6, floats like 4.5 and 6.7 and mixed like Python3"
        "456",
        "34567..689411",
        "34567.689411",
        "6.7",
        "Python3   6",
        "a1.2 b3 4.5 6 7.8 9 10",
        "45 6.9 87",
    ]

    for id, case in enumerate(cases_list):
        grand_total = 0

        print(f"\nCase #{id + 1}: \'{case}\'")

        floats_list = pluck_floats(case)
        print(f"floats_list = {floats_list}")
        floats_total = get_sum(floats_list)
        print(f"floats_total = {floats_total}")

        digits_list = pluck_digits(case)
        print(f"digits_list = {digits_list}")
        digits_total = get_sum(digits_list)
        print(f"digits_total = {digits_total}")

        grand_total = floats_total + digits_total
        print(f"the sum of all numerical values = {grand_total}")
        

if __name__ == "__main__":
    main()


"""
Case #1: 'Some text with numbers like 4,5 and 6, floats like 4.5 and 6.7 and mixed like Python3456'
floats_list = ['4.5', '6.7']
floats_total = 11.2
digits_list = ['4', '5', '6', '3', '4', '5', '6']
digits_total = 33.0
the sum of all numerical values = 44.2

Case #2: '34567..689411'
floats_list = []
floats_total = 0
digits_list = ['3', '4', '5', '6', '8', '9', '4', '1', '1']
digits_total = 41.0
the sum of all numerical values = 41.0

Case #3: '34567.689411'
floats_list = ['7.6']
floats_total = 7.6
digits_list = ['3', '4', '5', '6', '8', '9', '4', '1', '1']
digits_total = 41.0
the sum of all numerical values = 48.6

Case #4: '6.7'
floats_list = ['6.7']
floats_total = 6.7
digits_list = []
digits_total = 0
the sum of all numerical values = 6.7

Case #5: 'Python3   6'
floats_list = []
floats_total = 0
digits_list = ['3', '6']
digits_total = 9.0
the sum of all numerical values = 9.0

Case #6: 'a1.2 b3 4.5 6 7.8 9 10'
floats_list = ['1.2', '4.5', '7.8']
floats_total = 13.5
digits_list = ['3', '6', '9', '1', '0']
digits_total = 19.0
the sum of all numerical values = 32.5

Case #7: '45 6.9 87'
floats_list = ['6.9']
floats_total = 6.9
digits_list = ['4', '5', '8', '7']
digits_total = 24.0
the sum of all numerical values = 30.9
"""