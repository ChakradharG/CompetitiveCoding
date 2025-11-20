class BIT:
    def __init__(self, length):
        self.tree = [0 for _ in range(length)]

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
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cur = 0
        for i in range(n):
            if nums[i] == target:
                cur += 1
            else:
                cur -= 1
            nums[i] = cur

        indMap = {x: i for i, x in enumerate(sorted(set(nums + [0])))}
        bit = BIT(len(indMap)+1)
        bit.update(indMap[0]+1)

        ans = 0
        for num in nums:
            i = indMap[num]
            ans += bit.query(i)
            bit.update(i+1)
        return ans
