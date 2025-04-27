"""
Trip Planner: Given two list with prices of the flights. first list shows departure prices,
second list show return prices (D & R respecitively). Indices represent the dates.
Assumption is that departure and return cannot be on the same day and both lists are of the same length.
D = [10, 9, 8, 7, 11, 5]
R = [8, 8, 7, 15, 20, 18]
Output = 9 + 7 = 16
temp [18, 18, 15, 7, 7, 7]
"""

class Solution:
    def return_min_cost(self, D:list[int], R:list[int]) -> int:
        i = 0
        j = len(R) - 1
        n = len(D)
        cost = float('inf')
        temp = [0] * n
        temp[-1] = R[-1]
        for r in range(n - 2, -1, -1):
            temp[r] = min(R[r], temp[r + 1])
        for i in range(n - 1):
            cost = min(cost, D[i] + temp[i + 1])
    
        return cost

D = [10, 9, 8, 7, 11, 5]
R = [8, 8, 7, 15, 20, 18]

test = Solution()
print(test.return_min_cost(D, R))

D = [20, 15, 30, 5, 8]
R = [25, 10, 5, 20, 7]

test2 = Solution()
print(test2.return_min_cost(D,R))

D = [10, 9, 8, 7, 11, 5]
R = [20, 20, 20, 20, 20]

test3 = Solution()
print(test3.return_min_cost(D, R))