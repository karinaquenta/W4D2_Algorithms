#use recursion chain to break up groups the smallest as possible and plug them back
#compare smallest groups

input_list = [10,1,5,9,100,1,4,39,10,11,2]

def merge_sort(alist):
    middle = len(alist) //2 #find middle point - 2 halces
    left_half = alist[:middle]
    right_half = alist[middle:]

    #recrusicely call merge sort until groups of 1
    if len(alist)>1: #update input list greater than 1, then keep breakin it up
        merge_sort(left_half)
        merge_sort(right_half)
    #compare the elements from left had and right half plugging into list sorted
    #in place algo
    left_point = right_point = main_point = 0

    while left_point < len(left_half) and right_point < len(right_half):
        if left_half[left_point] < right_half[right_point]:
            alist[main_point] = left_half[left_point] # assign to list
            left_point += 1 #increment left pointer
            #main_point +=1#also increment left point
        else:
            alist[main_point]= right_half[right_point]
            right_point += 1
        main_point += 1
    #add any remaining elements from each list
    while left_point < len(left_half): #dont need to enter since they should be sorted
        alist[main_point] = left_half[left_point]
        left_point +=1
        main_point +=1

    while right_point < len(right_half):
        alist [main_point] = right_half[right_point]
        right_point +=1
        main_point +=1

merge_sort(input_list)
print(input_list)
