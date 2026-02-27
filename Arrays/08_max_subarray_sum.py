"""
Kadane's Algorithm : Maximum Subarray Sum in an Array

Problem Statement: Given an integer array nums,
find the subarray with the largest sum and return the sum of the elements present in that subarray.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [2, 3, 5, -2, 7, -4]  
Output: 15  
Explanation: The subarray from index 0 to index 4 has the largest sum = 15, 
which is the maximum sum of any contiguous subarray.

Example 2:
Input: nums = [-2, -3, -7, -2, -10, -4]  
Output:-2  
Explanation: The largest sum is -2, which comes from taking the element at index 0 or index 3 as the subarray. 
Since all numbers are negative, the subarray with the least negative number gives the largest sum.

"""

class Solution:
    def max_sub_srray(self,arr):
        n = len(arr)
        maxi = float('-inf')

        for i in range(n):
            
            for j in range(i, n):
                sum = 0

                for k in range(i,j+1):
                    sum += arr[k]
                
                maxi = max(maxi,sum)
        
        return maxi

solution = Solution()
print(solution.max_sub_srray([2, 3, 5, -2, 7, -4]))
print(solution.max_sub_srray([-2, -3, -7, -2, -10, -4]))