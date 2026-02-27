"""
Maximum Product Subarray in an Array

Problem Statement: Given an array that contains both negative and positive integers, 
find the maximum product subarray.

Input: Nums = [1,2,3,4,5,0]
Output: 120
Explanation: In the given array, 1x2x3x4x5 gives maximum product value.

Input: Nums = [1,2,-3,0,-4,-5]
Output: 20
Explanation: 
In the given array, (-4) x (-5) gives maximum product value.

"""

class Solution:
    def maxProductSubArray(self, arr):
        # Store length of array
        n = len(arr)

        # Initialize prefix and suffix products
        pre, suff = 1, 1

        # Initialize answer as negative infinity
        maxi_product = float('-inf')

        # Traverse from both front and back
        for i in range(n):
            # Reset prefix if zero
            if pre == 0:
                pre = 1

            # Reset suffix if zero
            if suff == 0:
                suff = 1

            # Multiply prefix with front element
            pre *= arr[i]

            # Multiply suffix with back element
            suff *= arr[n - i - 1]

            # Update maximum product so far
            maxi_product = max(maxi_product, pre, suff)

        # Return the result
        return maxi_product

# Sample usage
arr = [2, 3, -2, 4]
solution = Solution()
print(solution.maxProductSubArray(arr))
print(solution.maxProductSubArray([4, 5, 3, 7, 1, 2]))
print(solution.maxProductSubArray([-5, 0, -2]))
print(solution.maxProductSubArray([1, -2, 3, 4, -4, -3]))