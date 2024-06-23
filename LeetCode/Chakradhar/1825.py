from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.avg = 0
        self.sl = SortedList()
        self.q = deque([])

    def addElement(self, num: int) -> None:
        if (2 * self.k) <= len(self.q):
            n = len(self.q) - (2 * self.k)   # effective length
            if len(self.q) == self.m:   # remove oldest element
                prv = self.q.popleft()
                i = self.sl.index(prv)
                if i < self.k:
                    x = self.sl[self.k]
                elif self.k <= i < (self.m - self.k):
                    x = prv
                else:
                    x = self.sl[-self.k - 1]
                self.sl.remove(prv)
                self.avg = ((n * self.avg) - x) / max((n - 1), 1)
                n -= 1
            self.q.append(num)
            self.sl.add(num)
            j = self.sl.bisect_left(num)
            if j < self.k:
                y = self.sl[self.k]
            elif self.k <= j < (len(self.sl) - self.k):
                y = num
            else:
                y = self.sl[-self.k - 1]
            self.avg = ((n * self.avg) + y) / (n + 1)
        else:
            self.q.append(num)
            self.sl.add(num)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        else:
            return int(self.avg)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()