class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sn = sorted(nums)
        # sorted nums, a union will be a subarray in this with the parent 
        # being the smallest (leftmost) element of that subarray

        par = {sn[0]: 0}    # num -> index in sorted nums, parent map
        ptr = {0: 0}    # index -> index, to keep track of the next element to use in the particular union
        l, r = 0, 1
        while r < n:
            if (sn[r] - sn[r-1]) > limit:
                l = r
                ptr[l] = l
            par[sn[r]] = l
            r += 1

        for i in range(n):
            p = par[nums[i]]    # parent's index in sorted nums
            nums[i] = sn[ptr[p]]
            ptr[p] += 1

        return nums
