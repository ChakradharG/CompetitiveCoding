class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        heap = []
        for i in range(n):
            heap.append((nums[i], i))
            nums[i] = False # will be used for marking
        heapify(heap)

        score = 0
        while heap:
            num, i = heappop(heap)
            if not nums[i]:
                score += num
                nums[i] = True
                nums[max(0, i-1)] = True
                nums[min(n-1, i+1)] = True

        return score
