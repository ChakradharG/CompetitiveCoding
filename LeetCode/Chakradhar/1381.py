class CustomStack:

    def __init__(self, maxSize: int):
        self.l = []
        self.acc = [0 for _ in range(maxSize)]

    def push(self, x: int) -> None:
        if len(self.l) != len(self.acc):
            self.l.append(x)

    def pop(self) -> int:
        if len(self.l) == 0:
            return -1
        else:
            x = self.l.pop()
            i = len(self.l)
            x += self.acc[i]
            if i > 0:
                self.acc[i - 1] += self.acc[i]
            self.acc[i] = 0
            return x

    def increment(self, k: int, val: int) -> None:
        i = min(len(self.l), k) - 1
        if i > -1:
            self.acc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)