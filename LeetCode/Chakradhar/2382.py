class ListNode:
    def __init__(self, val=None, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


class Solution:
    def maximumSegmentSum(self, nums: list[int], removeQueries: list[int]) -> list[int]:
        n = len(removeQueries)

        pref = [0] * (n+1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        temp = sorted(removeQueries)
        d = {temp[0]: ListNode()}
        h = 0
        for i in range(n-1):
            l, r = temp[i], temp[i+1]
            x = ListNode(val=(pref[r]-pref[l+1]), prv=d[l])
            h = max(h, x.val)
            d[l].nxt = x
            d[r] = ListNode(prv=x)
            x.nxt = d[r]

        s, e = temp[0], temp[-1]
        x = ListNode(val=0, nxt=d[s])
        if s != 0:
            x.val = pref[s]
            h = max(h, x.val)
        d[s].prv = x
        x = ListNode(val=0, prv=d[e])
        if e != n-1:
            x.val = pref[n] - pref[e+1]
            h = max(h, x.val)
        d[e].nxt = x

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

