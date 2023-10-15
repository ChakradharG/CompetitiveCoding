# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heads = []
        for i in range(len(lists)):
            if lists[i]:
                heads.append(lists[i])
        if not heads:
            return

        for i in range(len(heads)):
            node = heads[i]
            while node:
                heapq.heappush(heap, node.val)
                prev = node
                node = node.next
            if i != len(heads)-1:
                prev.next = heads[i+1]

        node = heads[0]
        while node:
            node.val = heapq.heappop(heap)
            node = node.next

        return heads[0]
        