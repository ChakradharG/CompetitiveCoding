class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = deque([])
        while r < k:
            while q and q[-1] < nums[r]:
                # monotonically non-increasing queue
                q.pop()
            q.append(nums[r])
            r += 1

        ans = []
        while r < len(nums):
            ans.append(q[0])

            if nums[l] == q[0]:
                # if the max of current window is leftmost
                q.popleft()
            l += 1

            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            r += 1
        ans.append(q[0])

        return ans
