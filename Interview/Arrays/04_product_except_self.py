'''

Product of Array Except Self is a programming problem where, 
given an integer array nums, you must return a new array answer 
such that each element answer[i] equals the product of all elements in nums except nums[i] itself. 

For example:

Input: nums = [1, 2, 3, 4]
Output: answer = [24, 12, 8, 6]

    answer[0] = 2 x 3 x 4 = 24
    answer[1] = 1 x 3 x 4 = 12
    answer[2] = 1 x 2 x 4 = 8
    answer[3] = 1 x 2 x 3 = 6
'''

class Solution:
    def product_array(self,arr):
        product_arr = []
        for ele in arr:
            duplicate_arr = arr.copy()
            duplicate_arr.remove(ele)
            product = 1
            for num in duplicate_arr:
                product = product * num
            product_arr.append(product)
        return product_arr

solution = Solution()
print(solution.product_array([1, 2, 3, 4]))

