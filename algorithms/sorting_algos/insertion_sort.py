
num_list = [10,1,9,111,5,9,10]

def insertion_sort(alist): #1 pass thru and look at 1 # prev
    for i in range(1,len(alist)): #we want to start at 1
        current_value = alist[i] #extract but maintain code
        j = i - 1 #new index, outside before 0
        while current_value < alist[j] and j >= 0: #once either are false, plug current value to j +1 LINE 11
            alist[j+1] = alist[j] #move 10 to where 1 is
            j -= 1 #it takes it back
            alist[j+1] = current_value #plug value back in

insertion_sort(num_list)
print(num_list)

#As soon as we move a value, current_value ceases to
#  be in the list until we assign it a new index