def merge_sorted_lists(list1, list2):
    # Your code here
    po = []
    list1.extend(list2)
    list1.sort()
    po = list1
    return po

list11 = [1, 3, 5]
list12 = [2, 4, 6]
print(merge_sorted_lists(list11, list12))