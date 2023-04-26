#Bubble Sort
#Worst Case: O(n^2) Time - O(1) Space

num_list = [10,8,1,4,9,3,12]
def bubble_sort(alist):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]: #if current number is smaller then swap them
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_sorted = False #if false goes back up to while loop, if true DOES NOT start loop again
            print(alist)

bubble_sort(num_list)
print(num_list)
#with boundary
num_list = [10,8,1,4,9,3,12]
def bubble_sort(alist):
    is_sorted = False
    right_boundary = len(alist) -1 #right boundary last index on list
    while not is_sorted:
        is_sorted = True
        for i in range(right_boundary):
            if alist[i] > alist[i+1]: #if current number is smaller then swap them
                alist[i], alist[i+1] = alist[i+1], alist[i]
                is_sorted = False
        right_boundary -=1
        print(alist)

bubble_sort(num_list)
print(num_list)