"""
Given an array of integers nums, return the value of the largest element in the array

Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6
"""

class Solution:
    def largestElement(self, nums):
        self.nums = nums
        largest_element = self.nums[0]
        for ele in self.nums:
            if ele > largest_element:
                largest_element = ele
        return largest_element
        
obj = Solution()
collection_array = [3, 3, 6, 1]
largest_element = obj.largestElement(collection_array)
print(f"The largest element in array is {largest_element}")