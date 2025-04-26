"""
Given the root of a binary tree, 
imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example
                                       1    <-------- You are here
                                      / \
                                     /   \
                                    /     \
                                   /       \
                                  /         \
                                 /           \
                                /             \
                               /               \
                              /                 \
                             /                   \
                            /                     \
                           /                       \
                          /                         \
                         2                           3
                        / \                         / \
                       /   \                       /   \
                      /     \                     /     \
                     /       \                   /       \
                    /         \                 /         \
                   /           \               /           \
                  6             5             9             4
                 / \           / \
                /   \         /   \
               /     \       /     \
              N      null    7      8

Input: [1,2,3,6,5,9,4,null, null, 7,8]
Output: [1, 3, 4, 8]
Time Complexity: O(n) where each node is visited once
Space Complexity: O(w) wehre w is the maximum width of the tree

Analysis:
1. Create a queue (FIFO) with root as the starting node
2. Create a right view list
3. Loop over each level from top to bottom
4. Add to the queue if queue is not nonde
5. loop through each iteration where i in range(len(queue))
6. popleft the element
7. If i == len(queue) - 1, append the popped element to right_view
8. If node.left or node.right -> append to queue
"""

class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        
        right_view = []
        queue = deque([root])

        while queue:
            print(len(queue))
            for i in range(len(queue)):
                node = queue.popleft()
                if i == len(queue) - 1: # It means it is the last element in the queue
                    right_view.append(node.val)
                    print(right_view)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return right_view


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3, TreeNode(9), TreeNode(4))
root.left.left = TreeNode(6)
root.left.right = TreeNode(5, TreeNode(7), TreeNode(8))

def print_tree(root: TreeNode):
    if root:
        print(root.val, end =" ")
        print_tree(root.left)
        print_tree(root.right)

test = Solution()
#print_tree(root)
print(test.rightSideView(root))


    
