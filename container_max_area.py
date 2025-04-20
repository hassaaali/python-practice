"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Analysis:
1. max_area = max(distance between indices) * height[i]
2. Create two pointer left and right.
3. Move the pointers while calculating the max current area and comparing the previous stored value
4. return the max area in the end.

Time complexity will be O(n) to traverse all the elements within height
Space complexity will be O(1) to store index and area values
"""

class Solution:
    def maxArea(self, height:list[int]) -> int:
        r_index = len(height) - 1
        l_index = 0
        area = 0
        while l_index < r_index:
            distance = r_index - l_index
            if height[l_index] < height[r_index]:
                area = max(area, distance * height[l_index])
                l_index += 1
            else:
                area = max(area, distance * height[r_index])
                r_index -= 1

        return area

# Test Case
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test = Solution()
print(test.maxArea(height))
