#in-place mutates our input, such as .sort()
#cant mutate string, strings are immutable

random_list = [9,2,10,1,100,4]
random_list.sort()
#print(random_list)
# [1, 2, 4, 9, 10, 100]

random_list_2 = [100,1,5,3]
#out of plalce sorted()
sorted_list_2 = sorted(random_list_2)
print(sorted_list_2) #[1, 3, 5, 100]
print(random_list_2) #[100, 1, 5, 3]

def swap_indecies(alist,index1,index2):
    alist[index1] = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = index1_value

num_list = [9,10,1,2]
swap_indecies(num_list, 1, 2)  

print(num_list)

def swap_indecies(alist,index1,index2):
    alist[index1],alist[index2] = alist[index2], alist[index1]
    return alist

new_list = swap_indexes([2,5,10,3], 0, -1)
print(new_list)

def swap_indecies(alist,index1,index2):
    alist[index1],alist[index2] = alist[index2], alist[index1] #updatin order of value
    return alist



#Class Ex:

l_1 = [1,2]
def swap_indices_ex(list, ind1, ind2, ind3):
    list[ind1], list[ind2], list[ind3] = list[ind3], list[ind1], list[ind2]
    return list

swap_indices_ex(1_1,1,2,3)
print(l_1)