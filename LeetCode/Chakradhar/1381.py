class CustomStack:

    def __init__(self, maxSize: int):
        self.l = []
        self.k = maxSize

    def push(self, x: int) -> None:
        if len(self.l) != self.k:
            self.l.append(x)

    def pop(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            return self.l.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.l), k)):
            self.l[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)