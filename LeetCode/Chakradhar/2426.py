class BIT:
    def __init__(self, l):
        self.tree = [0 for _ in range(l)]   # cnt <= i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def update(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            i += (i & -i)

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = []
        mn, mx = math.inf, -math.inf
        for n1, n2 in zip(nums1, nums2):
            x = n1 - n2
            nums.append(x)
            mn = min(mn, x)
            mx = max(mx, x)

        for i in range(len(nums)):
            nums[i] = nums[i] - mn + 1
        mx = mx - mn + 1

        bit = BIT(mx + 1)
        ans = 0
        cmn, cmx = math.inf, -math.inf
        for j, num in enumerate(nums):
            x = num + diff + 1
            if x < cmn:
                pass
            elif x >= cmx:
                ans += j
            else:
                ans += bit.query(x)
            bit.update(num + 1)
            cmn = min(cmn, num + 1)
            cmx = max(cmx, num + 1)

        return ans
