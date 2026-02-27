"""
Given an integer array arr of size N, sorted in ascending order (with distinct values), 
the array is rotated at any index which is unknown. Find the minimum element in the array.

Example 1:
    Input: arr = [4,5,6,7,0,1,2,3]
    Output: 0
    Explanation: The minimum element in the array is 0.

Example 2:
    Input : arr = [3,4,5,1,2]
    Output: 1
    Explanation : The minimum element in the array is 1.

"""
class Solution:
    def find_minimum(self,arr):
        minimun_ele = arr[0]
        for ele in arr:
            if ele <= minimun_ele:
                minimun_ele = ele
        
        return minimun_ele

solution = Solution()
print(solution.find_minimum([4,5,6,7,0,1,2,3]))
print(solution.find_minimum([3,4,5,1,2]))
print(solution.find_minimum([3,4,-5,1,-2]))