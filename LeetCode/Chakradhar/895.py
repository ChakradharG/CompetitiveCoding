class FreqStack:

    def __init__(self):
        self.h = []
        self.c = {}
        self.counter = 0

    def push(self, val: int) -> None:
        if val not in self.c:
            self.c[val] = [0, 0]
        self.c[val][0] += 1
        self.c[val][1] = self.counter
        self.counter += 1
        heapq.heappush(self.h, (-self.c[val][0], -self.c[val][1], val))

    def pop(self) -> int:
        *_, val = heapq.heappop(self.h)
        self.c[val][0] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()