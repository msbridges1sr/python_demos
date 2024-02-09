# Makes a temp deepcopy of the original list sorts the temp list lowest to highest
# deepcopies the temp_list back to the original list and deletes the temp_list.
# The sort is done with an outer for loop and an inner for loop. The outer for loop
# iterates the number of times there are items, calling the inner for loop.
# The inner for loop takes each item in the list and compares it the item ahead of 
# it in the list. If it is smaller it changes place and continues the loop.
# This produces a list that has left-to-righ high-to-low values, so at the end
# the list is reversed.
import copy

list = [4 , 1, 3, 9, 7]
temp_list = copy.deepcopy(list)
print('Deepcopy of list, temp_list: ', temp_list)

for item in range(0, len(temp_list), 1):
    print(f'\nPass number = {item}\n')
    for index in range(0, len(temp_list)-1, 1):
        print(f"Index: {index}, temp_list element: {temp_list[index]}")
        curr_element = temp_list[index]
        next_element = temp_list[index+1]
        print(f'curr_element = {curr_element}, next_element = {next_element}')
        if curr_element < next_element:
            print('curr_element is less than next_element, swapping..')
            temp_list[index+1] = curr_element
            temp_list[index] = next_element
        print('list_in_progress = ', temp_list)
temp_list.reverse()
print('Finished, sorted temp_list low-high = ', temp_list)

print('Deep copying temp_list to list, and deleting temp_list..')
list = copy.deepcopy(temp_list)
del(temp_list)
print('Final sorted list = ', list)
