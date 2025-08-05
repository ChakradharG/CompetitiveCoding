class BIT:
    def __init__(self, length):
        self.tree = [0 for _ in range(length)] # tree[i] = cnt of (<=doubled[i])

    def query(self, v):
        res = 0
        while v > 0:
            res += self.tree[v]
            v -= (v & -v)
        return res

    def update(self, v):
        while v < len(self.tree):
            self.tree[v] += 1
            v += (v & -v)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        doubled = sorted([2 * num for num in nums])

        bit = BIT(len(nums) + 1)
        ans = 0
        for num in reversed(nums):
            ans += bit.query(bisect_left(doubled, num)) # number of elements seen so far that are than num
            bit.update(bisect_left(doubled, 2 * num) + 1)   # add 2*num to seen

        return ans
