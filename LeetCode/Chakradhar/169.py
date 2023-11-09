class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == ans:
                cnt += 1
            else:
                if cnt == 0:
                    ans = nums[i]
                    cnt += 1
                else:
                    cnt -= 1

        return ans

# Ref: https://www.youtube.com/watch?v=7pnhv842keE
# Ref: https://www.youtube.com/watch?v=nP_ns3uSh80
