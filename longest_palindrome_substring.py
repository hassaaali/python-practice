"""
Given a string s, return the longest palindromic substring in s.
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Time complexity: O(n^2)
Space complexity: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        
        start, max_len = 0, 1

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start, max_len = left, right - left + 1

                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start, max_len = left, right - left + 1
                
                left -= 1
                right += 1
            
        return s[start:start + max_len]
        