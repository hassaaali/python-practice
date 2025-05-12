class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


def print_list(head: ListNode) -> None:
    curr = head
    while curr:
        print(curr.val, end= "->")
        curr = curr.next

head = ListNode(1)
head.next = ListNode(9)
head.next.next = ListNode(2)
head.next.next.next = ListNode(7)
test = Solution()
reverse = test.reverse(head)
print_list(reverse)

