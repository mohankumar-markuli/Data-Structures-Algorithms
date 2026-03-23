"""
Given an integer array nums, sorted in ascending order (with distinct values) and a target value k.
The array is rotated at some pivot point that is unknown. 
Find the index at which k is present and if k is not present return -1.

Example 1
Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output: 4
    Explanation: Here, the target is 0. 
    We can see that 0 is present in the given rotated sorted array, nums. Thus, 
    we get output as 4, which is the index at which 0 is present in the array.

Example 2
Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output: -1
    Explanation: Here, the target is 3. 
    Since 3 is not present in the given rotated sorted array. 
    Thus, we get the output as -1.

"""

class Solution:
    def search(self, nums, k):
        for val in nums:
            if val == k:
                return nums.index(val)
        return -1

solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2],0))
print(solution.search([4, 5, 6, 7, 0, 1, 2],3))
print(solution.search([4, 5, 6, 7, 0, 1, 2],5))
