class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        p, s = 0, 0
        maxH, minH = [], []
        for i in range(n):
            j = 3*n-i-1
            p += nums[i]
            maxH.append(-nums[i])
            s += nums[j]
            minH.append(nums[j])
        heapify(maxH)
        heapify(minH)

        pref, suff = {n-1:p}, {2*n-1:s}
        for i in range(n, 2*n):
            j = 3*n-i-1
            heappush(maxH, -nums[i])
            p += (nums[i] + heappop(maxH))
            pref[i] = p
            heappush(minH, nums[j])
            s += (nums[j] - heappop(minH))
            suff[j-1] = s

        ans = pref[n-1] - suff[n-1]
        for i in range(n, 2*n):
            ans = min(ans, pref[i] - suff[i])

        return ans
