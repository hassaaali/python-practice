"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Time complexity is O(n)
Space complexity is O(h)
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
# Example Usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(10)
root.left.left = TreeNode(1)

test = Solution()
max_depth = test.maxDepth(root)

print(max_depth)


