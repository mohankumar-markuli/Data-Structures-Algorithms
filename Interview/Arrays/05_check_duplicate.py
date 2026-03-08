"""
Problem Statement: Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.


Example 1:
    Input: nums = [1, 2, 3, 1]
    Output: true.
    Explanation: 1 appeared two times in the input array.

Example 2: 
    Input: nums = [1, 2, 3, 4]
    Output: false
    Explanation: input array does not contain any duplicate number. 

"""

class Solution:
    def check_duplicate(self,arr):
        arr_set = set(arr)
        if len(arr) == len(arr_set):
            return False
        else:
            return True
        
solution = Solution()
print(solution.check_duplicate([1,2,3,1]))
print(solution.check_duplicate([1,2,3,4]))