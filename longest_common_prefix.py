"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Analysis:
1. Sort the array by length of elements
2. len(strs[0]) will be the limit equal to i
3. first = strs[0]
4. while i > 0, check if first[0:i] in strs[1:]
5. if yes, return first[0:i] else return ""

Highest time complexity will be that of sorting: O(n log(n))
Space complexity will be O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            char = strs[0][i]
            for word in strs[1:]:
                if word[i] != char:
                    return strs[0][:i]
            
        return strs[0][:min_len]

    

# Test case
test = Solution()
strs = ["flower","flow","flight", "fl"]
print(test.longestCommonPrefix(strs))