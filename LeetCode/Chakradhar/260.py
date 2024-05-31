class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num

        bit = 1
        while not (res & bit):
            bit <<= 1

        a, b = 0, 0
        for num in nums:
            if (num & bit):
                a ^= num
            else:
                b ^= num

        return [a, b]
