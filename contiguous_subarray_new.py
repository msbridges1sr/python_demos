from typing import List, Dict, Tuple

def find_max_sum(case_num_list: List[int]) -> Tuple[Dict[int, List[List[int]]], List[int], List[int], int]:
    """
    Find the contiguous sub-list within a list of integers that has the maximum sum.

    Args:
        case_num_list (List[int]): The list of integers to analyze.

    Returns:
        sublists_by_sum (Dict[int, List[List[int]]]): Dictionary mapping sums to corresponding sublists.
        contig_totals_list (List[int]): List of cumulative sums.
        max_sub_list (List[int]): Sublist with the highest sum.
        max_sum (int): Highest sum found among all possible sublists.
    """

    if not case_num_list:  # Handle empty input list
        return {}, [], [], float('-inf')

    contig_totals_list = []
    sublists_by_sum = {}
    running_total = 0
    max_sum = float('-inf')  # Ensure first max_sum check on first number in case_num_list is higher
    max_sub_list = []
    start_idx = 0

    for i in range(len(case_num_list)):
        running_total += case_num_list[i]
        contig_totals_list.append(running_total)

        # Update max_sum and max_sub_list if necessary
        if running_total > max_sum:
            max_sum = running_total
            max_sub_list = case_num_list[start_idx:i+1]  # Slice of case_num_list that makes max_sum

        # Add the current sub-list to sublists_by_sum 
        if running_total in sublists_by_sum:
            sublists_by_sum[running_total].append(case_num_list[start_idx:i+1])  # Add running_total's sub_list under same running total if found in sublists_by_sum 
        else:
            sublists_by_sum[running_total] = [case_num_list[start_idx:i+1]]  # Add new running_total's sub_list to sublists_by_sum 

        # Reset running_total and start_idx to exclude negative contributions
        if running_total < 0:
            running_total = 0
            start_idx = i + 1

    return sublists_by_sum, contig_totals_list, max_sub_list, max_sum

def main():
    case_list = [
        [],
        [1, 2, 3, -2, 5],
        [3, 4, 5, 6, -19, 2, 4],
        [-4, -3, -3, -3, -2],
        [-4, -3, 30, -3, -3, -3],
        [-4, -3, -1, -3, -3, -3]
    ]
    for case_id, sublist in enumerate(case_list):
        if not sublist:  # Handle empty sublist directly
            print(f'\nCase #{case_id + 1}: {sublist}\nCase list empty, try again.')
            continue

        print(f'\nCase #{case_id + 1}: {sublist}')
        sublists_by_sum, contig_totals_list, max_sub_list, max_sum = find_max_sum(sublist)
        print(f'sublists_by_sum: {sublists_by_sum}')
        print(f'contig_totals_list: {contig_totals_list}')
        print(f'contiguous sub-list with maximum sum: {max_sub_list} (sum: {max_sum})')

if __name__ == "__main__":
    main()


"""
Case #1: []
Case list empty, try again.

Case #2: [1, 2, 3, -2, 5]
sublists_by_sum: {1: [[1]], 3: [[1, 2]], 6: [[1, 2, 3]], 4: [[1, 2, 3, -2]], 9: [[1, 2, 3, -2, 5]]}
contig_totals_list: [1, 3, 6, 4, 9]
contiguous sub-list with maximum sum: [1, 2, 3, -2, 5] (sum: 9)

Case #3: [3, 4, 5, 6, -19, 2, 4]
sublists_by_sum: {3: [[3]], 7: [[3, 4]], 12: [[3, 4, 5]], 18: [[3, 4, 5, 6]], -1: [[3, 4, 5, 6, -19]], 2: [[2]], 6: [[2, 4]]}
contig_totals_list: [3, 7, 12, 18, -1, 2, 6]
contiguous sub-list with maximum sum: [3, 4, 5, 6] (sum: 18)

Case #4: [-4, -3, -3, -3, -2]
sublists_by_sum: {-4: [[-4]], -3: [[-3], [-3], [-3]], -2: [[-2]]}
contig_totals_list: [-4, -3, -3, -3, -2]
contiguous sub-list with maximum sum: [-2] (sum: -2)

Case #5: [-4, -3, 30, -3, -3, -3]
sublists_by_sum: {-4: [[-4]], -3: [[-3]], 30: [[30]], 27: [[30, -3]], 24: [[30, -3, -3]], 21: [[30, -3, -3, -3]]}
contig_totals_list: [-4, -3, 30, 27, 24, 21]
contiguous sub-list with maximum sum: [30] (sum: 30)

Case #6: [-4, -3, -1, -3, -3, -3]
sublists_by_sum: {-4: [[-4]], -3: [[-3], [-3], [-3], [-3]], -1: [[-1]]}
contig_totals_list: [-4, -3, -1, -3, -3, -3]
contiguous sub-list with maximum sum: [-1] (sum: -1)
"""