"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Analysis:
1. Create a min heap by import heapq. min heap ensures that in a binary tree, root is the smallest and it's children are
    always greater than root. root.right > root.left child
2. Add val, index and node to min heap for all given k linked-lists to startwith. 
3. Create a dummy_head to store the sorted linked list
4. Create a current pointer to dummy head
5. while heap -> add heappop to current.next
6. If node.next -> heappush (val, index, node.next)
7. Return dummy_head.next

Time Complexity: Insert opertaion in min heap takes O(log k) and pop takes O(log k). So, time complexity will be O(nlog(k)),
    where k is the number of elements in min heap and n is the number of nodes within each linked list. 2n number of operations
    for each heappush and heappop.
Space Complexity: Space complexity will be O(k), where is k is the number of elements stored in the heap at any given time.
    Ignoring result linked-list because it is just returning the result and not part of the opertions.
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists:
            return None

        import heapq
        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        dummy_head = ListNode()
        current = dummy_head

        while min_heap:
            # heappop returns the smallest value
            val, index, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy_head.next
    


# Example Usage

def print_list(merged_list: ListNode) -> None:
    curr = merged_list
    while curr:
        print(curr.val, end="->")
        curr = curr.next

if __name__ == "__main__":
    l1 = ListNode(3, ListNode(4, ListNode(5)))
    l2 = ListNode(2, ListNode(7))
    l3 = ListNode(8, ListNode(1))

lists = [l1, l2, l3]
print(lists)

test = Solution()
merged_list = test.mergeKLists(lists)

print_list(merged_list)