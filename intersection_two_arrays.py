"""
Given two integer arrays nums1 and nums2, 
return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Analysis:
1. loop through the first array
2. See if the element exists in the second array
3. Append it to result array if not already present

Time complexity will be O(m * n) wehre m and n are elements of the array 1 and 2. 
Space complexity will be O(min(m,n))
"""

class Solution:
    def intersection (self, nums1: list[int], nums2: list[int]) -> list[int]:
        if nums1 is None or nums2 is None:
            return []
        result = []
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        
        return result
    
# Test Case

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
test = Solution()
print(test.intersection(nums1, nums2))
