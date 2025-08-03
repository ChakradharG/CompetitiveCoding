class BIT:
    def __init__(self, a):
        mn, mx = math.inf, -math.inf
        for num in a:
            mn = min(mn, num)
            mx = max(mx, num)
        self.mn = mn
        self.tree = [0 for _ in range(mx-mn+2)] # self.tree[i] = number of elements smaller than or equal to i

    def query(self, i):
        i = i - self.mn + 1
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= (i & -i)
        return ans

    def update(self, i, d):
        i = i - self.mn + 1
        while i < len(self.tree):
            self.tree[i] += d
            i += (i & -i)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        bit = BIT(nums)
        for num in nums:
            bit.update(num, +1)

        ans = []
        for num in nums:
            bit.update(num, -1)
            ans.append(bit.query(num-1))

        return ans
