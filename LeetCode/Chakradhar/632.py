class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        ptrs, h = [], []
        mx = -math.inf
        for i in range(k):
            ptrs.append(1)
            h.append((nums[i][0], i))
            mx = max(mx, nums[i][0])
        heapify(h)
        mn = h[0][0]

        ans = [mn, mx]
        while True:
            x, i = heappop(h)
            if ptrs[i] == len(nums[i]):
                break
            y = nums[i][ptrs[i]]
            heappush(h, (y, i))
            ptrs[i] += 1
            mn, mx = h[0][0], max(mx, y)
            if (mx - mn) < (ans[1] - ans[0]):
                ans = [mn, mx]

        return ans
