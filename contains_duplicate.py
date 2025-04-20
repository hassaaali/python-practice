"""
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Time complexity will O(n) as it iterates through all the elements of the list and adding to a set.
Space Complexity will be O(n) for storing the values in set.
"""
class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
