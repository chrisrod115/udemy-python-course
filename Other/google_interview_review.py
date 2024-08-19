# take a collection of numbers and find a matching pair == sum
# [1,2,3,9] sum = 8
# [1,2,4,4] sum = 8

"""
Inputs: two arrays 
Outputs: bool --> true or false
Space and time? --> 

Are the arrays sorted? 
Will the numbers in both arrays be integers?
Is the output I will provide fine?

First approach: Use two for loops --> iterate index by index to find the sum i.e (1 + 2) == sum?  (1 + 3)
    Issue: o(n^2) time

Second approach: (sorted)
# [1,2,3,9] sum = 8
   L     R 
"""
def matching_pair(arr1, sum):
    left, right = 0, len(arr1) - 1
    
#   [1,2,3,9] sum = 8
#      L R 
    while left < right:
        if (arr1[left] + arr1[right]) > sum:
            right -= 1
        
        if (arr1[left] + arr1[right]) < sum:
            left += 1
        
        if (arr1[left] + arr1[right]) == sum:
            return True
    return False

a1 = [1,2,3,9] 
a2 = [1,2,4,4] 
sum = 8

print(matching_pair(a1, sum))
print(matching_pair(a2, sum))