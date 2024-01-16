class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = [[]]
        self.num = 1
        self.idx = [0]

    def push(self, val: int) -> None:
        while self.idx and self.idx[0] > self.num-1:
            heapq.heappop(self.idx)
        if not self.idx:
            self.idx = [self.num-1]
        lidx = self.idx[0]
        self.stacks[lidx].append(val)
        if len(self.stacks[lidx]) == self.cap:
            while self.idx and self.idx[0] == lidx:
                heapq.heappop(self.idx)
            if lidx == self.num-1:
                self.stacks.append([])
                self.num += 1
            if len(self.idx) == 0:
                self.idx.append(self.num-1)

    def pop(self) -> int:
        while self.num > 1 and not self.stacks[-1]:
            self.stacks.pop()
            self.num -= 1
        if not self.stacks[-1]:
            self.idx = [0]
            return -1
        else:
            return self.stacks[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index > self.num-1 or not self.stacks[index]:
            return -1
        else:
            heapq.heappush(self.idx, index)
            return self.stacks[index].pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)