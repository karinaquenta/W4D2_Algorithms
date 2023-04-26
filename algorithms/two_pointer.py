#reverse a list using a 2 pointer approach
#1--
# def reverse_list(alist):
#     left, right = 0, len(alist) -1 #2 variables on the left line
#     while left < right: 
#         alist[left], alist[right] = alist[right], alist[left] #flipping
#         left +=1 #continues til left is equal or more 
#         right -= 1

# alist = [1,2,3,4,5,6,7,8,9]
# #we will reverse the order
# reverse_list(alist)
# print(alist)
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
#2---
def reverse_list(alist, left, right):
    while left < right: 
        alist[left], alist[right] = alist[right], alist[left] #flipping
        left +=1 #continues til left is equal or more 
        right -= 1

alist = [1,2,3,4,5,6,7,8,9]
#we will reverse the order
reverse_list(alist, 2, -1)
#print(alist)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
'racecar'
'racercar'
'apple'
def check_palindrome(astring):
    left, right = 0, len(astring) -1
 #beg word is 0,last position is -1
    while left < right:
        left_letter = astring[left]
        right_letter = astring[right]
        print(left_letter, right_letter)
        if left_letter != right_letter:
            return False 
        left +=1
        right -=1 #make sure it goes down, if out of range, check right pointer
    return True

print(check_palindrome('racecar'))
print(check_palindrome('matrix'))    