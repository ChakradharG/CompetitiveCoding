class BIT:
    def __init__(self, length):
        self.tree = [0 for _ in range(length)]

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def update(self, i, diff):
        while i < len(self.tree):
            self.tree[i] += diff
            i += (i & -i)

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        ind = {v: i for i, v in enumerate(sorted(set(nums)))}
        bit = BIT(len(ind)+1)

        l, r = 0, 0
        cur = 0
        while r < k:
            num = nums[r]
            i = ind[num]
            cur += (r - bit.query(i+1))
            bit.update(i+1, +1)
            r += 1

        ans = cur
        while r < len(nums):
            #rem
            num = nums[l]
            i = ind[num]
            cur -= bit.query(i)
            bit.update(i+1, -1)

            #add
            num = nums[r]
            i = ind[num]
            cur += ((k-1) - bit.query(i+1))
            bit.update(i+1, +1)

            ans = min(ans, cur)
            l, r = l + 1, r + 1

        return ans
