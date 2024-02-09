# Sorts a list of numbers lowest to highest, left/right in a temp copy of the original
# It iterates the temp list culling out the smallest value using the min() function, writing 
# it to a new list then removing it from the temp list. It then deletes the empty temp list.
# this is not a'bubbling' however, see bubble_sort.py.

import copy

list = [4 , 1, 3, 9, 7]
print('list =', list)
temp_list = copy.deepcopy(list)
print('Deepcopy of list, temp_list: ', temp_list)
new_list = []

for index in range(0, len(temp_list), 1):
    #print('index =', index)
    min_val = min(temp_list)
    #print('min_val = ', min_val)
    new_list.append(min_val)
    temp_list.remove(min_val)
    print('new_list =  ', new_list)

print('deleting temp_list because it is empty:', temp_list)
del(temp_list)
