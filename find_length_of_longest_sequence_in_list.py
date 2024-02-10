# This program takes an unordered list of integers and identifies the presence of sequences within it.
# It then identifies the length of the longest_sequence found.
# It uses an outter for loop to iterate each element in the list.
# If the current element has its next number found, it proceeds to the inner while loop which checks for 
# the next numbers in squence until there are no more found. The count of the sequence is saved as well
# as the numbers touched by the process. As each element is iterated, it is first checked whether it has
# already been used by the process to avoid processing numbers redundantly. The useful key word is 'in'
# for searching the list data structure.

list = [1, 9, 3, 10, 4, 20, 2]
used_element_list = []
seq_length_list = []

for index in range(0, len(list), 1):
    i = 1
    seq_len = 1
    curr_value = list[index]
    print('index = ', index, 'curr_value = ', curr_value)
    if curr_value in used_element_list:
        continue
    else:
        used_element_list.append(curr_value)

    search_next_value = curr_value + i
    if search_next_value in list:
        seq_len += 1
        print(f'for: yes, {search_next_value} is in the list')
        used_element_list.append(search_next_value)
        print('used_element_list = ', used_element_list)
        
        while search_next_value != 0:
            search_next_value +=i
            print('while: search_next_value = ', search_next_value)
            if search_next_value in used_element_list:
                break
            if search_next_value in list:
                seq_len += 1
                print(f'while: yes, {search_next_value} is in the list')
                used_element_list.append(search_next_value)
                print('used_element_list = ', used_element_list)
            else:
                print(f'while: no, {search_next_value} is not in the list')
                print('while: seq_len = ', seq_len)
                seq_length_list.append(seq_len)
                search_next_value = 0
    else:
        print(f'no, {search_next_value} is not in the list')

print('used_element_list = ', used_element_list)
print('seq_length_list = ', seq_length_list)
longest_sequence = max(seq_length_list)
print('longest_sequence = ', longest_sequence)
