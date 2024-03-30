class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cur, cnt = 0, 0
        d = defaultdict(int)
        l, r = 0, 0

        while r < len(nums):
            if d[nums[r]] == 0:
                cur += 1
            d[nums[r]] += 1

            while cur > k:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    cur -= 1
                l += 1
            if cur == k:
                j = r + 1
                while j < len(nums) and d[nums[j]] != 0:
                    j += 1
                i = l
                while cur == k:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        cur -= 1
                    l += 1
                cnt += (l - i) * (j - r)

            r += 1

        return cnt
