### linaer Search

```
Given an array of n elements and a target value x, the task is to find the index of the first occurrence of x in the array. 
If x is not present in the array, return -1. 
```
Example 1
```   
    Input: nums = [2, 5, 7, 3, 42, 35, 7, 76], target = 42
    Output: 4
    Explanation: Because nums[4] == 42, we return 4.
```
Example 2
```
    Input: nums = ["mohan","abd","markuli"], target = "abd"
    Output: 1
```
Example 3
```
    Input: nums = ["mohan", 3, 4, 5, "abd", "markuli"], target = 7
    Output: -1
```
Constraints: 
```
Best Case: O(1) — when the target is at the first position. 
Worst Case: O(n) — when the target is at the last position or not present. 
Average Case: O(n)
```