def bubble_sort(numbers):
    """
    Sorts a list of numeric elements from highest to lowest.

    Args:
        numbers (list): List of numeric elements to be sorted.

    Returns:
        list: The same list sorted in descending order.
    """
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def main():
    print(f'\nUsing the algorithm..')
    test_list = [4, 1, 3, -9, -7]
    print(f'Unsorted list:         {test_list}')
    print(f'Sorted list decending: {bubble_sort(test_list)}')
    print(f'\nUsing the standard function \'sorted()\'..')
    
    test_list2 = [4, 1, 3, -9, -7]
    sorted_numbers = sorted(test_list2, reverse=True)
    print(f'Unsorted list2:        {test_list2}')
    print(f'Sorted list decending: {sorted_numbers}\n') 

if __name__ == '__main__':
    main()


"""
Using the algorithm..
Unsorted list:         [4, 1, 3, -9, -7]
Sorted list decending: [4, 3, 1, -7, -9]

Using the standard function 'sorted()'..
Unsorted list2:        [4, 1, 3, -9, -7]
Sorted list decending: [4, 3, 1, -7, -9]
"""