from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList()
        cnt = 0
        for num in nums:
            i = sl.bisect_right(2 * num)
            cnt += (len(sl) - i)
            sl.add(num)

        return cnt
