class Window:
    def __init__(self, nums: List[int]) -> None:
        self.w = set()
        self.cost = 0
        self.nums = nums
    def __len__(self) -> int:
        return len(self.w)
    def __contains__(self, index: int) -> bool:
        return index in self.w
    def add(self, index: int) -> None:
        self.w.add(index)
        self.cost += self.nums[index]
    def discard(self, index: int) -> None:
        if index in self.w:
            self.cost -= self.nums[index]
        self.w.discard(index)

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k -= 1 # the window does not contain the first element since it is always fixed
        maxheap, minheap = [], []
        window = Window(nums) # currently chosen subarray start indices
        ans = math.inf
        l, r  = 1, 1
        while r < n:
            # add the new elem to minheap and choose the smallest elem not currently chosen
            heappush(minheap, (nums[r], r))
            val, ind = heappop(minheap)
            window.add(ind)
            heappush(maxheap, (-val, ind))
            # shrink the window
            if (r - l) > dist:
                window.discard(l)
                l += 1
            # remove stale elems as well as elems outside of the window
            while maxheap and (maxheap[0][1] < l or maxheap[0][1] not in window):
                val, ind = heappop(maxheap)
            # remove stale elems as well as elems outside of the window
            while minheap and (minheap[0][1] < l or minheap[0][1] in window):
                heappop(minheap)
            if len(window) < k and minheap:
                val, ind = heappop(minheap)
                heappush(maxheap, (-val, ind))
                window.add(ind)
            if len(window) > k:
                window.discard(maxheap[0][1])
                val, ind = heappop(maxheap)
                heappush(minheap, (-val, ind))
            if len(window) == k:
                ans = min(ans, window.cost)
            r += 1

        return nums[0] + ans

