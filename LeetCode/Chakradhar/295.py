class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []

    def balance(self):
        if len(self.maxH) - len(self.minH) > 1:
            heapq.heappush(self.minH, -heapq.heappop(self.maxH))
        elif len(self.maxH) - len(self.minH) < -1:
            heapq.heappush(self.maxH, -heapq.heappop(self.minH))

    def addNum(self, num: int) -> None:
        if self.maxH and num <= -self.maxH[0]:
            heapq.heappush(self.maxH, -num)
        else:
            heapq.heappush(self.minH, num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.maxH) > len(self.minH):
            return -self.maxH[0]
        elif len(self.maxH) < len(self.minH):
            return self.minH[0]
        else:
            return (self.minH[0] - self.maxH[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()