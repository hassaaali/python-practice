"""
Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output = 5

Analysis:
1. Profit will be maximized when prices[right_pointer] - prices[left_pointer] is maximum
2. If prices[left_pointer + 1] < princes[left_pointer] -> left_pointer + 1
3. If prices[right_pointer - 1] > princes[left_pointer] -> right_pointer - 1
4. Loop till left_pointer < right_pointer
5. return prices[right_pointer] - prices[left_pointer]

Time complexity will be O(n) where n is the number of elements in the prices array
Space Complexity will be O(1) for storing the pointer positions
"""

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        current_profit = 0

        while right_pointer < len(prices):
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer
            else:
                current_profit = max(current_profit, prices[right_pointer] - prices[left_pointer])
            
            right_pointer += 1
        return current_profit

# Test Case
prices = [2, 1, 2, 0, 1]
test = Solution()
print(test.maxProfit(prices))




