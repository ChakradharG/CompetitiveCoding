class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        cur = 0
        for num in nums:
            cur += num
            diff = cur - k
            cnt += prefix[diff]
            prefix[cur] += 1

        return cnt