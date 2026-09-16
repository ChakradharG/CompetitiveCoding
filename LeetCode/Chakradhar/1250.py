class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = nums[0]
        for num in nums:
            g = gcd(g, num)

        return g == 1

