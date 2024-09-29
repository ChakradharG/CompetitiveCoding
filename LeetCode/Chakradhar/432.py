class AllOne:

    def __init__(self):
        self.n = 0
        self.d = {}
        self.c = defaultdict(set)
        self.c[0].add('')
        self.mn, self.mx = math.inf, 0

    def inc(self, key: str) -> None:
        if key not in self.d:
            self.c[1].add(key)
            self.d[key] = 1
            self.n += 1
        else:
            v = self.d[key]
            self.c[v].remove(key)
            self.c[v+1].add(key)
            self.d[key] += 1
        self.mx = max(self.mx, self.d[key])
        self.mn = min(self.mn, self.d[key])

    def dec(self, key: str) -> None:
        v = self.d[key]
        self.d[key] -= 1
        self.c[v].remove(key)
        if v == 1:
            del self.d[key]
            self.n -= 1
        else:
            self.c[v-1].add(key)
            self.mn = min(self.mn, self.d[key])

    def getMaxKey(self) -> str:
        if self.n == 0:
            return ''
        while len(self.c[self.mx]) == 0:
            self.mx -= 1
        return next(iter(self.c[self.mx]))

    def getMinKey(self) -> str:
        if self.n == 0:
            return ''
        while len(self.c[self.mn]) == 0:
            self.mn += 1
        return next(iter(self.c[self.mn]))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()