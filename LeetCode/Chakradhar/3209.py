class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # the idea is that AND is a monotonic decreasing function
        # adding more values either decreases the AND value or keeps it the same
        # so, if we look at all the subarrays ending at a particular index and track
        # the number of unique AND values, it will never be > 32 (number of bits)
        # this is because when we start at index i and go left ANDing values,
        # once a bit is reset, it can never be set again.
        unique = defaultdict(int)
        ans = 0
        for num in nums:
            new = defaultdict(int)
            new[num] = 1
            for key, v in unique.items():
                new[key & num] += v
            unique = new
            ans += unique[k]

        return ans
