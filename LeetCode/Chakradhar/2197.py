class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        stack = []
        for num in nums:
            while stack and (g := gcd(stack[-1], num)) != 1:
                num = stack.pop() * num // g
            stack.append(num)

        return stack
