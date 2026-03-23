"""
Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward. 
For example, 121, 1331, and 4554 are palindromes because they remain 
the same when their digits are reversed.

Example 1
    Input: n = 121
    Output: true
    Explanation: When read from left to right : 121.
    When read from right to left : 121.

Example 2
    Input: n = 123
    Output: false
    Explanation: When read from left to right : 123.
    When read from right to left : 321.
"""

class Solution:
    def isPalindrome(self, n):
        n_toString = str(n)
        if n_toString == n_toString[::-1]:
            return True
        return False
    
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(123))
