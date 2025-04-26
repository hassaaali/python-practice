"""
Given a binary tree, assume you are standing on the bottom left side of the tree.
Print the tree starting from bottom letf and then assume you are standing on the right side,
print right side from top to bottom to reach the starting node

          7
         /  \
        2    4
        / \   \
        4   3  8
         \ 
          5
Input: [7, 2, 4, 4, 3, None, 8, None, 5]
Output: [5, 4, 2, 7, 4, 8]

"""

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Time complexity is O(n)
Space complexity is O(n) -> O(queue + leftmost_path + rightmost_path)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def leftmost_path(self, root: TreeNode) -> list[int]:
        if not root or not root.left:
            return []
        queue = deque([root.left])
        left_values = []
        while queue:
            level = len(queue)
            for i in range(level):
                node= queue.popleft()

                if i == level - 1:
                    left_values.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return left_values


    def rightmost_path(self, node: TreeNode) -> list[int]:
        right_values = []
        while node:
            right_values.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        
        return right_values
    
    def fullpath(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        left_path = self.leftmost_path(root)
        left_path.reverse()
        right_path = self.rightmost_path(root)

        return left_path + right_path
    
root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
root.right.right = TreeNode(8)
root.left.right.right = TreeNode(5)
test = Solution()
print(test.fullpath(root))


        
    

            
        





