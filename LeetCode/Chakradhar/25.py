# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        slow, fast = head, head
        linker = head
        while fast:
            for i in range(k):
                if not fast:
                    return head
                fast = fast.next

            prev = fast
            curStart = slow
            while slow != fast:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            if linker == head:
                head = prev
            else:
                linker.next = prev
                linker = curStart

        return head
