"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Analysis:
1. If not grid -> return
2. Get rows and columns of grid
3. visited = set()
4. islands = 0
5. make two for loops on rows and columns
6. Do depht first search if value is not in visited and value is 1.

Time complexity will be O(m*n)
Space complexity will be O(m * n). Best case, it will O(1) where visited is not used at all.
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    self.dfs(grid, row, col, visited)
                    islands += 1

        return islands

    def dfs(self, grid:list[list[str]], row: int, col: int, visited: set) -> None:
        if row < 0 or row >= len(grid) \
        or col < 0 or col >= len(grid[0]) \
        or (row, col) in visited \
        or grid[row][col] == '0':
            return
        visited.add((row, col))
        self.dfs(grid, row + 1, col, visited)
        self.dfs(grid, row - 1, col, visited)
        self.dfs(grid, row, col + 1, visited)
        self.dfs(grid, row, col - 1, visited)


# Example usage
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
test = Solution()
print(test.numIslands(grid))