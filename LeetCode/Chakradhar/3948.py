class MEX:
    def __init__(self):
        self.d = defaultdict(int)
        self.mex = 0
    def add(self, x):
        self.d[x] += 1
        if x == self.mex:
            while self.d[self.mex] != 0:
                self.mex += 1
    def rem(self, x):
        self.d[x] -= 1
        if self.d[x] == 0 and x < self.mex:
            self.mex = x

class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        total = MEX()
        for num in nums:
            total.add(num)

        result = []
        pref = MEX()
        l = 0
        for r in range(len(nums)):
            pref.add(nums[r])
            if pref.mex == total.mex:
                result.append(pref.mex)
                while l <= r:
                    total.rem(nums[l])
                    pref.rem(nums[l])
                    l += 1

        return result
