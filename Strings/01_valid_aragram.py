"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1

Input : s = "anagram" , t = "nagaram"
Output : true
Explanation :We can rearrange the characters of string s to get string t 
as frequency of all characters from both strings is same.

Example 2
Input : s = "dog" , t = "cat"
Output : false
Explanation : We cannot rearrange the characters of string s 
to get string t as frequency of all characters from both strings is not same.

"""

class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here

        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t):
            return True
        return True
    
sol = Solution()
print(sol.anagramStrings("dog","cat"))
print(sol.anagramStrings("anagram","nagaram"))