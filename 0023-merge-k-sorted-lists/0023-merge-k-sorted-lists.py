# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        head = ListNode()
        heap = [(node.val, i, node) for i, node in enumerate(lists) if isinstance(node, ListNode)]
        heapq.heapify(heap)
        current = head

        while heap:
            _, i, minimal_node = heapq.heappop(heap)
            current.next = minimal_node
            current = current.next
            candidate = minimal_node.next
            if candidate:
                heapq.heappush(heap, (candidate.val, i, candidate))
        return head.next

