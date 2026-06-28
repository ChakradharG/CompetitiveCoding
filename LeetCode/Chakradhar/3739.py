class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # if we transform nums such that trn[i] = +1 if (nums[i] == target) else -1
        # then this problem essentially becomes finding subarrays of trn with sum > 0
        # if we maintain a prefix sum on trn, then the number of subarrays ending at any
        # given index i is the count of indices j < i such that pref[j] < pref[i]
        # a neat trick to efficiently find count of indices j is to maintain the count
        # of subarrays seen thus far with prefix value less than current one and update
        # it during each iteration
        pref = defaultdict(int) # count of prefixes
        p = 0 # current prefix
        pref[p] = 1
        cnt, ans = 0, 0 # subarrays seen thus far with prefix value less than p, final answer
        for num in nums:
            if num == target:
                # since p is incrementing by 1, add the number of prefixes p seen thus far
                cnt += pref[p]
                p += 1
            else:
                # since p is decrementing by 1, remove the number of prefixes p-1 seen thus far
                p -= 1
                cnt -= pref[p]
            ans += cnt # add number of valid subarrays ending at the current index to the final answer
            pref[p] += 1 # record current prefix

        return ans
