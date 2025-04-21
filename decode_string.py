"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Analysis:
1. Create a stack which will save (current_str, current_num)
2. Create a variable current_num = 0 and current_str = ""
3. if s[i].isdigit(), current_num = s[i]
4. if s[i] == '[' -> append current_str and current_num. Reset both of them
5. if s[i] == ']' -> pop the stack  to get last_str and repeat_count
6. updated current_str = last_str + current_str * repeat_count
7. else: current_str += s[i]

Time complexity will be O(n)
Space complexity will be O(1)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_num = 0
                current_str = ""
            elif char == ']':
                last_str, repeat_count = stack.pop()
                current_str = last_str + current_str * repeat_count
            else:
                current_str += char
        return current_str
    
# Test case
s = "100[leetcode]"
test = Solution()
print(test.decodeString(s))

        
        