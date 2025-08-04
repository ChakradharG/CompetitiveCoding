class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        self.tree = [0 for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            self.build(i, num)

    def build(self, index: int, val: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += (index & -index)

    def update(self, index: int, val: int) -> None:
        delta = val - self.a[index]
        self.a[index] = val
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += (index & -index)

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        while left > 0:
            res -= self.tree[left]
            left -= (left & -left)
        right += 1
        while right > 0:
            res += self.tree[right]
            right -= (right & -right)
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)