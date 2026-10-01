class ListNode:
    def __init__(self, val=None, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(removeQueries)
        d = {0: ListNode(prv=ListNode(val=0), nxt=ListNode(val=0))}
        h = 0
        for i in range(1, n):
            d[i] = ListNode(prv=d[i-1].nxt, nxt=ListNode(val=0))
            d[i-1].nxt.nxt = d[i]


        ans = [0] * n
        for i in reversed(range(n)):
            ans[i] = h
            j = removeQueries[i]
            l, r = d[j].prv, d[j].nxt
            l.val += (nums[j] + r.val)
            l.nxt = r.nxt
            if l.nxt is not None:
                l.nxt.prv = l
            h = max(h, l.val)

        return ans

