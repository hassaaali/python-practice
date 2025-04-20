"""
Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:

The height of the tree is height and the number of rows m should be equal to height + 1.
The number of columns n should be equal to 2height+1 - 1.
Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
Continue this process until all the nodes in the tree have been placed.
Any empty cells should contain the empty string "".
Return the constructed matrix res.

Analaysis:
1. Recursively get height of the binary tree
2. n = 2^(height + 1) - 1 and m = height + 1
3. create a mxn mattrix with deafult value ""
4. TreeNode(0) should be placed at res[0][(n - 1)/2]
5. root.left = res[r+1][c-2**(height-r-1)]
6. right.child = res[r+1][c+2**(height-r-1)]
7. return the res matrix

Time complexity for getting height of the tree will be O(n) since each node will be visited during BFS.
Space complexity will be O(n) since both the matrix and queue require space proportional to the number of nodes

"""
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_height(self, root: TreeNode) -> int:
        if root is None:
            return -1
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        return 1 + max(left_height, right_height)
    
    def printTree(self, root: TreeNode) -> list[list[str]]:
        if root is None:
            return []

        height = self.get_height(root)
        m = height + 1
        n = 2**(m) - 1
        
        res = [["" for _ in range(n)] for _ in range(m)]
        queue = deque([(root, 0, (n - 1) // 2)])
        while queue:
            node, r, c = queue.popleft()
            res[r][c] = str(node.val)

            if node.left:
                queue.append((node.left, r + 1, c - 2**(height - r - 1)))
            if node.right:
                queue.append((node.right, r + 1, c + 2**(height - r - 1)))
        
        return res
        





#Test Case
tree = TreeNode(1)
tree.left = TreeNode(2)

test = Solution()
print(test.printTree(tree))