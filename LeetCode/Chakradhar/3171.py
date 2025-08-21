class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        unique = set()
        ans = math.inf

        for num in nums:
            new = {num}
            for un in unique:
                new.add(num | un)
            unique = new
            for un in unique:
                ans = min(ans, abs(k - un))

            if ans == 0:
                break

        return ans
