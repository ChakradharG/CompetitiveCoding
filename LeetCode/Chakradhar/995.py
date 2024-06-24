class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        q = deque([])
        for i in range(n):
            if (len(q) > 0) and (i - q[0] >= k):
                q.popleft()
            if (nums[i] + len(q)) % 2 == 0:
                if i > (n - k):
                    return -1
                else:
                    cnt += 1
                    q.append(i)

        return cnt
