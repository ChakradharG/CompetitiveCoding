class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        acc, MOD = 0, 10**9 + 7
        stack = [(-math.inf, -1)]

        for i, x in enumerate(arr + [-math.inf]):
            while x < stack[-1][0]:
                val, j = stack.pop()
                left = j - stack[-1][1]
                right = i - j
                acc = (acc + (val * (left * right))) % MOD
            stack.append((x, i))

        return acc
