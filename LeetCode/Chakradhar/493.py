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
        mapping = {
            v: i for i, v in enumerate(
                sorted(set(nums) | {2*num for num in nums})
            )
        }

        bit = BIT(len(mapping) + 1)
        ans = 0
        for i, num in enumerate(nums):
            ans += (i - bit.query(mapping[2*num] + 1)) # number of elements seen so far that are > than 2*num
            bit.update(mapping[num] + 1)   # add num to seen

        return ans
