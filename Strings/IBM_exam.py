"""
input = ['(','(())','((()(())']
output = [1,1,0]

"""

class Solution:    
    def anagramStrings(self, par_list):
        result = []
        for val in par_list:
            if len(val) == 0:
                result.append(0)
            elif val.count('(') == val.count(')'):
                result.append(1)
            else:
                result.append(0)
        return result
sol = Solution()
print(sol.anagramStrings(['(','(())','((()(())','']))
