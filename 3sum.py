"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Analysis:
1. Sort the list
2. loop through th list
3. Define left = i + 1, right = n - 1
4. total = nums[i] + nums[j] + nums[k]
5. if total < 0 -> move left pointer by 1
6. If total > 0 -> move right pointer less by 1
7. Else, append to result array
8.  While left < right and nums[left] == nums[left + 1], move left by 2 instead of 1 to avoid duplicates
9.  While left < right and nums[right] == nums[right - 1], move right less by 2 instead of 1 to avoid duplicates
10. Same for i in the begining of the for loop. If i > 0 and nums[i] == nums[i - 1], continue

Time complexity: O(n^2). Sorting takes O(n log (n)) but the prior is greater.
Space complexity: O(1) since we are using constant space variables i, left, right.
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result  = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result
    

# Example Usage
nums = [-1,0,1,2,-1,-4]
test = Solution()
print(test.threeSum(nums))
