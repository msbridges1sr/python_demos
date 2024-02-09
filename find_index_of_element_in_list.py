# Find index of an element in a list

list = [5, 6, 7, 8, 9, 10, 10, 2, 3]
search_value = 10

for index in range(0, len(list), 1):
    list_value = list[index]
    print(f'index = {index}, list_value = {list_value}')
    if list_value == search_value:
        print('Output: ', index)
