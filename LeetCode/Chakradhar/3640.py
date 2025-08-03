class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        nums.append(-math.inf)
        n = len(nums)
        ans, cur = -math.inf, nums[0]
        l, r = 0, 1
        up, dn = 0, 0
        while r < n:
            if up == 0 and dn == 0:
                if nums[r-1] < nums[r]:
                    # next
                    up = 1
                    cur += nums[r]
                else:
                    # reset
                    l = r
                    cur = nums[l]
            elif up == 1 and dn == 0:
                if nums[r-1] < nums[r]:
                    # continue
                    cur += nums[r]
                    while l < r-1 and nums[l] < 0:
                        cur -= nums[l]
                        l += 1
                elif nums[r-1] == nums[r]:
                    # reset
                    l = r
                    cur = nums[l]
                    up, dn = 0, 0
                else:
                    # next
                    dn = 1
                    cur += nums[r]
            elif up == 1 and dn == 1:
                if nums[r-1] < nums[r]:
                    # next
                    up += 1
                    cur += nums[r]
                elif nums[r-1] == nums[r]:
                    # reset
                    l = r
                    cur = nums[l]
                    up, dn = 0, 0
                else:
                    # continue
                    cur += nums[r]
            else:
                ans = max(ans, cur)
                if nums[r-1] < nums[r]:
                    # continue
                    cur += nums[r]
                elif nums[r-1] == nums[r]:
                    # reset
                    l = r
                    cur = nums[l]
                    up, dn = 0, 0
                else:
                    # next (cycle)
                    l = r - 2
                    cur = nums[l] + nums[l+1] + nums[r]
                    up, dn = 1, 1
                    while nums[l-1] < nums[l] and nums[l-1] > 0:
                        cur += nums[l-1]
                        l -= 1
            r += 1

        return ans
