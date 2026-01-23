class ListNode:
    def __init__(self, ind, val=0):
        self.ind = ind
        self.val = val
        self.prv = None
        self.nxt = None

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        h = []  # (nums[i] + nums[right of i], i, node)
        curSum = {}   # i: nums[i] + nums[right of i]
        cnt = 0 # pairs out of order

        head = ListNode(-1, -math.inf)
        prv, i = head, 0
        for num in nums+[math.inf]:
            node = ListNode(i, num)
            node.prv, prv.nxt = prv, node
            if 0 < i < n:
                s = prv.val + node.val
                heappush(h, (s, i-1, prv))
                curSum[i-1] = s
                if prv.val > node.val:
                    cnt += 1
            prv = node
            i += 1
        tail = prv

        ans = 0
        while cnt:
            s, i, node = heappop(h)
            if s != curSum[i] or node.nxt is tail:
                continue

            l, r = node, node.nxt
            cnt -= (l.prv.val > l.val) + (l.val > r.val) + (r.val > r.nxt.val)
            node.val = s
            node.nxt, r.nxt.prv = r.nxt, node
            curSum[r.ind] = -math.inf

            if node.prv is not head:
                j = node.prv.ind
                curSum[j] = node.prv.val + node.val
                heappush(h, (curSum[j], j, node.prv))
                cnt += (node.prv.val > node.val)

            if node.nxt is not tail:
                curSum[i] = node.val + node.nxt.val
                heappush(h, (curSum[i], i, node))
                cnt += (node.val > node.nxt.val)

            ans += 1

        return ans
