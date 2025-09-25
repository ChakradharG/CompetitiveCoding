class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.inv = defaultdict(dict)   # s: {m: [p, available]}
        self.m2s = defaultdict(list)    # m: [(p, s)]
        self.rented = []    # p, s, m
        self.fm2s = set()   # avoid duplicates in heap
        self.frented = set()    # avoid duplicates in heap
        for s, m, p in entries:
            self.inv[s][m] = [p, True]
            self.m2s[m].append((p, s))
            self.fm2s.add((m, s))
        for s in self.m2s.values():
            heapify(s)

    def search(self, movie: int) -> List[int]:
        res = []
        while self.m2s[movie] and len(res) < 5:
            price, shop = heappop(self.m2s[movie])
            self.fm2s.remove((movie, shop))
            if self.inv[shop][movie][1]:
                res.append(shop)
        for shop in res:
            price = self.inv[shop][movie][0]
            heappush(self.m2s[movie], (price, shop))
            self.fm2s.add((movie, shop))
        return res

    def rent(self, shop: int, movie: int) -> None:
        price = self.inv[shop][movie][0]
        self.inv[shop][movie][1] = False
        if (movie, shop) not in self.frented:
            heappush(self.rented, (price, shop, movie))
            self.frented.add((movie, shop))

    def drop(self, shop: int, movie: int) -> None:
        price = self.inv[shop][movie][0]
        self.inv[shop][movie][1] = True
        if (movie, shop) not in self.fm2s:
            heappush(self.m2s[movie], (price, shop))
            self.fm2s.add((movie, shop))

    def report(self) -> List[List[int]]:
        res = []
        while self.rented and len(res) < 5:
            price, shop, movie = heappop(self.rented)
            self.frented.remove((movie, shop))
            if not self.inv[shop][movie][1]:
                res.append((shop, movie))
        for (shop, movie) in res:
            price = self.inv[shop][movie][0]
            heappush(self.rented, (price, shop, movie))
            self.frented.add((movie, shop))
        return res

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
