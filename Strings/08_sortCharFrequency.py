"""
You are given a string s. Return the array of unique characters, 
sorted by highest to lowest occurring characters.
If two or more characters have same frequency then arrange them in alphabetic order.

Input : s = "tree"
Output : ['e', 'r', 't' ]
Explanation : The occurrences of each character are as shown below :

e --> 2
r --> 1
t --> 1.

The r and t have same occurrences , so we arrange them by alphabetic order.
"""

class Solution:
    def frequencySort(self, s: str):
        dict_count = {}
        n = len(s)
        for i in range(0,n):
            if s[i] in dict_count:
                dict_count[s[i]]+=1
            else:
                dict_count[s[i]] = 1
        return sorted(dict_count)

sol = Solution()
sol.frequencySort("tree")