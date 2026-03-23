"""
Given an array arr[] of non-negative integers, 
where each element arr[i] represents the height of the vertical lines,
 find the maximum amount of water that can be contained between any two lines, 
 together with the x-axis.

Input: arr[] = [1, 5, 4, 3]
Output: 6
    Explanation: 5 and 3 are 2 distance apart. So the size of the base = 2. 
    Height of container = min(5, 3) = 3. So total area = 3 * 2 = 6.

Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
    Explanation: 5 and 3 are 4 distance apart. So the size of the base = 4. 
    Height of container = min(5, 3) = 3. So total area = 4 * 3 = 12.

Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
    Explanation: 8 and 5 are 5 distance apart. So the size of the base = 5. 
    Height of container = min(8, 5) = 5. So, total area = 5 * 5 = 25.
 
"""

class Solution:
    def max_water_container(self,arr):
        n = len(arr)
        result = 0

        for i in range(n):
            for j in range(i+1,n):
                amount = min(arr[i],arr[j]) * (j-i)
                result = max(amount,result)
        return result


solution = Solution()
print(solution.max_water_container([3, 1, 2, 4, 5]))