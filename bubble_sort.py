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
    test_list = [4, 1, 3, 9, 7]
    print(f'Unsorted list:         {test_list}')
    print(f'Sorted list decending: {bubble_sort(test_list)}')

if __name__ == '__main__':
    main()
