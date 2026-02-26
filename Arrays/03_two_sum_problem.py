"""
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.
Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in increasing order.

Example 1
    Input: nums = [1, 6, 2, 10, 3], target = 7
    Output: [0, 1]
Explanation:
    nums[0] + nums[1] = 1 + 6 = 7

Example 2
    Input: nums = [1, 3, 5, -7, 6, -3], target = 0
    Output: [1, 5]

Explanation:
    nums[1] + nums[5] = 3 + (-3) = 0
"""

class Solution:
    def twoSum(self, nums, target):
        for num in nums:
            duplicate_list = nums.copy()
            duplicate_list.remove(num)
            number = num
            for element in duplicate_list:
                if target == element + number:
                    return [nums.index(number),nums.index(element)]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) # [0,1]
print(solution.twoSum([3,2,4], 6)) # [1,2]
print(solution.twoSum([3,3], 6)) # [0,1]
