
from typing import List, Tuple


def find_longest_seq(case_list: List[int]) -> Tuple[List[int], int]:
    """
    Finds longest contiguous sequence of positive numbers in an unsequenced list.
    Prints first occurence of a sequence with max length found in the list.
    Counts occurances of sequences of max length.
    Uses a list of lists to gather the sequences from the case_list for analysis.
    Uses a list of lists to drive test cases.  

    Args:
        case_list(List[int]): List of numbers to analyze.

    Returns:
        longest_seq_list(List[int]): List with longest contiguous sequence.
        max_len(int): Length of longest contiguous sequence. 
        occurences_max_len_str (string) = Count of sequences with max length found.

    """

    max_len = 0
    index_of_max = 0
    current_value = 0
    next_value = 0
    seq_list = [0]
    results_list = []
    longest_seq_list = []
    len_subs_str = ''
    occurences_max_len_str = ''


    # If empty case_list, return
    if len(case_list) == 0:
        return longest_seq_list, max_len, occurences_max_len_str
    
   # If non-integers in case_list, return
    all_integers = all(isinstance(x, int) for x in case_list)
    if not all_integers:
        return longest_seq_list, max_len, occurences_max_len_str

    # Find sequences in case_list
    for index, item in enumerate(case_list):
        
        # If end of case_list, break
        if index + 1 == len(case_list): 
            if len(seq_list) > 1:
                results_list.append(seq_list)
            break

        # Get current and next values
        current_value = case_list[index]
        next_value = case_list[index + 1]

        # If next item in case_list is in-sequence, save its index and loop

        if current_value + 1 == next_value:
            seq_list.append(index + 1)
            continue

        # If next item not in-sequence, reset seq_list if necessary
        else:
            if len(seq_list) > 1:
                results_list.append(seq_list)
                seq_list = []
                seq_list = [index + 1]

    # If empty results_list, return
    if len(results_list) == 0:
        return longest_seq_list, max_len, occurences_max_len_str
    
    # Find length of the longest sublist
    for index, sublist in enumerate(results_list):
        len_sub = len(results_list[index])

        if len_sub > max_len:
            max_len = len_sub
            index_of_max = index

        # Count occurences of sublists of max length
        len_subs_str = len_subs_str + str(len_sub)
        max_len_str = str(max_len)
        occurences_max_len_str = str(len_subs_str.count(max_len_str))

    # Return longest sublist and its length
    longest_seq_list = results_list[index_of_max]
    return longest_seq_list, max_len, occurences_max_len_str


def main():
    cases_list = [
        [1, 2, 3],  # Only seq (3)
        [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15],  # Longest sequence (3) in the beginning of list, (4) occurences
        [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15],  # Longest sequence (6) in middle of list
        [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17],  # Longest sequence (9) at end of list
        [1, 3, 5, 7, 9],  # no contiguous sequences
        [-1, -2, 5, -7, -8],  # no contiguous sequences
        ['a', 'b', 'c'],  # no contiguous sequences
        []  # no contiguous sequences
    ]

    # Run variety of sublists in the cases_list
    for id, case in enumerate(cases_list):
        print(f'\nCase #{id+1}: {case}')
        longest_seq_list, max_len, occurences_max_len_str = find_longest_seq(case)
        if max_len < 2:
            print(f'No contiguous sequences found')
        else:
            if int(occurences_max_len_str) > 1:
                print(f'First of {occurences_max_len_str} sequences of max length: {longest_seq_list}, max length: {max_len}')
            else:
                print(f'Longest sequence of max length: {longest_seq_list}, max length: {max_len}')

if __name__  == '__main__':
    main()


"""
Case #1: [1, 2, 3]
Longest sequence of max length: [0, 1, 2], max length: 3

Case #2: [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15]
First of 4 sequences of max length: [0, 1, 2], max length: 3

Case #3: [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]
Longest sequence of max length: [3, 4, 5, 6, 7, 8], max length: 6

Case #4: [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
Longest sequence of max length: [6, 7, 8, 9, 10, 11, 12, 13, 14], max length: 9

Case #5: [1, 3, 5, 7, 9]
No contiguous sequences found

Case #6: [-1, -2, 5, -7, -8]
No contiguous sequences found

Case #7: ['a', 'b', 'c']
No contiguous sequences found

Case #8: []
No contiguous sequences found
"""