class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def calc_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd = numsDivide[0]
        for i in range(1, len(numsDivide)):
            gcd = calc_gcd(gcd, numsDivide[i])

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > gcd:
                return -1
            elif gcd % nums[i] == 0:
                return i

        return -1
