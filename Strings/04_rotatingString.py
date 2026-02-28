"""
Given two strings s and goal, 
return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, 
input: "abcde" and 1
output: "bcdea
"""
class Solution:    
    def rotateString(self, s, goal):
        #your code goes here
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False
    
solution = Solution()
print(solution.rotateString("abcde","bcdea"))