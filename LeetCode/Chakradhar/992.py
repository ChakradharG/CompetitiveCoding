class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cur, cnt = 0, 0
        d = defaultdict(int)
        j, l, r = 0, 0, 0

        while r < len(nums):
            d[nums[r]] += 1
            if d[nums[r]] == 1:
                cur += 1

            while cur > k:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    cur -= 1
                l += 1
                j = l

            while d[nums[l]] > 1:
                d[nums[l]] -= 1
                l += 1

            if cur == k:
                cnt += (l - j + 1)

            r += 1

        return cnt
