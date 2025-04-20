"""
You are given a string s consisting of digits and an integer k.

A round can be completed if the length of s is greater than k. In one round, do the following:

Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.
Return s after all rounds have been completed.

Analysis:
1. loop and form groups from i to k, appending to groups intialized in the beginning
2. Sum each group and add it to s
3. Use recursion to bring the sum within k limit


Time complexity: In each round, the string reduces by n/k, resulting O(log(n)) and work per round is O(n) is has to
    loop through the whole string on length n. Hence, the time complexity is O(n.log(n))
Space complexity will be O(n) as n/k groups are formed. As new_s is bounded by O(n), space complexity will remain the same.
"""

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        groups = []
        for i in range(0, len(s), k):
            groups.append(s[i:i + k])
        new_s = ""
        for group in groups:
            res = 0
            for digit in group:
                res += int(digit)
            new_s += str(res)
        return self.digitSum(new_s, k)



# Test case

s = "11111222223"
k = 3
test = Solution()
print(test.digitSum(s, k))
            
