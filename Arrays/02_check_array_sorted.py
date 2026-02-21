"""
Given an array nums of n integers, 
return true if the array nums is sorted in non-decreasing order or else false.

Example 1
    Input : nums = [1, 2, 3, 4, 5]
    Output : true

Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], 
hence it is sorted and we return true.

Example 2
Input : nums = [1, 2, 1, 4, 5]
Output : false

Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], 
hence it is not sorted and we return false.
"""

class Solution:
    def isSorted(self, nums):
        previous_element = 0
        for element in nums:
            if element >= previous_element:
                previous_element = element
                continue
            else:
                return False
        return True
        
obj = Solution()
collection_array = [1, 2, 1, 4, 5]
largest_element = obj.isSorted(collection_array)

if largest_element is True:
    print(f"The array is Sorted")
else:
    print("The array is not Sorted")