"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Analysis:
1. while l1 and l2
2. if l1.next == l2.next -> return l1.next

Time complexity will be O(l1 + l2)
Space complexity will be constant O(1)
"""

class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution():
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return
        
        currA = headA
        currB = headB

        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
        return currA

# Test Case
headA = ListNode('a1')
headA.next = ListNode('a2')
headA.next.next = ListNode('c1')

headB = ListNode('b1')
headB.next = ListNode('b2')
headB.next.next = ListNode('b3')
headB.next.next.next = headA.next.next

def print_node(head: ListNode) -> str:
    print(head.val if head else None)

test = Solution()
intersection = test.getIntersectionNode(headA, headB)
print_node(intersection)