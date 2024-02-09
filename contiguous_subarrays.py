# This program takes a list of integers (positive or negative), and finds the contiguous sub-list
# with the maximum sum. It iterates the list calculating a running total. In each iteration, it saves
# the total into a totals list and b) saves to a dictionary using that total as the key and storing
# sub-list of integers making that total as the value. At the end it finds the highest total in the 
# totals list, and uses that as the key to find the sub-list of integers in the dictionary.

list = [1, 2, 3, -2, 5]
print('list = ', list)
contig_totals_list = []
contig_dict = {}
total = 0
i = 0

for i in range(i, len(list), 1):
    total = total + list[i]
    print('total = ', total)
    contig_totals_list.append(total)
    if i == 0:
        slice_of_list = list[0]
    else:
        slice_of_list = list[0 : i+1]
        contig_dict.setdefault(total, slice_of_list)
        print('contig_dict= ', contig_dict)

print('contig_totals_list', contig_totals_list)
high_total = max(contig_totals_list)
print('high_total', high_total)
print(f"This contiguous subset of numbers: {contig_dict[high_total]} has the maximum sum of: {high_total}")
