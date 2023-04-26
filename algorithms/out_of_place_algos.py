#returns updated copy & we have original list
def swap_out_of_place(alist, index1, index2):
    alist_copy = alist[::] #make a copy of our list from beg to end
    alist_copy[index1], alist_copy[index2] = alist_copy[index2], alist_copy[index1]#flip elements at given indexes
    return alist_copy
swapped_list = swap_out_of_place([1,2,3,4,5,10], 2, -1) #to swap last ele
print(swapped_list)
#[1, 2, 10, 4, 5, 3]