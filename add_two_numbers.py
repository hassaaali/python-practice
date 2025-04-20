"""
Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explaination: 342 + 465 = 807

Assumptions:


Steps to Solve:
1. Create a ListNode class with val and next pointer
2. Initialize a variable carry with zero
3. while l1 or l2 or carry -> keeping adding the result to a result ListNode
5. carry is calculated by total % 10

Time Complexity will be O(max(n, m)) where n is the elements in l1 and m are the elements in l2
Space Complexity will be O(max(n, m)) which stores n elements in result. If there is a carry, it will be O(max(n, m)) + O(1)
 but O(1) can be ignored since O(max(n, m)) will be greater.
"""

class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2:list[ListNode]) -> list[ListNode]:
        result = ListNode()
        curr = result
        carry = 0
        while l1 or l2 or carry:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0)+ carry
            carry = total // 10
            total = total % 10
            
            curr.next = ListNode(total)
            curr = curr.next
            # check l1.next to make sure it is none None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next

# Exampl Usage
l1 = ListNode(val= 2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
# l1 = [2, 4, 3]

l2 = ListNode(val = 7)
l2.next = ListNode(0)
l2.next.next = ListNode(8)

#l2 = [7, 0, 8]

# Expected outcome: 342 + 807 = 1149 So, result array should be [9, 4, 1, 1]
def print_list(head: ListNode):
    curr = head
    while curr:
        print(curr.val, end = "->")
        curr = curr.next


test = Solution()
result = test.addTwoNumbers(l1, l2)
print_list(result)