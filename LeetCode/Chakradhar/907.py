class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        acc, MOD = 0, 10**9 + 7
        arr = [-math.inf] + arr + [-math.inf]
        stack = []

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j+1
                right = i - j
                acc = (acc + m * left * right) % MOD
            stack.append((i, n))

        return acc
