class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sn = sorted(nums)
        par = {sn[0]: 0}    # num -> index
        ptr = {0: 0}    # index -> index
        l, r = 0, 1
        while r < n:
            if (sn[r] - sn[r-1]) > limit:
                l = r
                ptr[l] = l
            par[sn[r]] = l
            r += 1

        for i in range(n):
            p = par[nums[i]]
            nums[i] = sn[ptr[p]]
            ptr[p] += 1

        return nums
