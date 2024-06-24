def find_index(search_list, search_value):
    """
    Finds the index of search_value in search_list.

    Args:
        search_list (List[int]): The list of items to analyze.
        search_value (int): The value to get index of.

    Returns:
        index (int): The index of value in search_list.
    """
    for index, item in enumerate(search_list):
        if item == search_value:
            return index
        
def built_in_find(search_list, search_value):
    return search_list.index(search_value)

def main():
    search_list = [5, 6, 7, 8, 9, 10, 10, 2, 3]
    search_value = 10
    print(
        f"Using algorithm 'find_index()' the index of {search_value} is "
        f"[{find_index(search_list, search_value)}]"
    ) 
    print(
        f"Using the built-in function .. the index of {search_value} is "
        f"[{built_in_find(search_list, search_value)}]")

if __name__ == '__main__':
    main()


"""
Using algorithm 'find_index()' the index of 10 is [5]
Using the built-in function .. the index of 10 is [5]
"""