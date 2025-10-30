class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[-1]
        for i in range(1, len(target)):
            if target[i-1] > target[i]:
                ans += (target[i-1] - target[i])

        return ans
