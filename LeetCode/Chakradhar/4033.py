class Window:
    def __init__(self, nums):
        self.s = self.e = 0
        self.odd = self.unq = 0
        self.freq = defaultdict(int)
        self.nums = nums

    def add(self, i):
        self.freq[self.nums[i]] += 1
        if self.freq[self.nums[i]] % 2:
            self.odd += 1
        else:
            self.odd -= 1
        if self.freq[self.nums[i]] == 1:
            self.unq += 1

    def rem(self, i):
        self.freq[self.nums[i]] -= 1
        if self.freq[self.nums[i]] % 2:
            self.odd += 1
        else:
            self.odd -= 1
        if self.freq[self.nums[i]] == 0:
            self.unq -= 1


class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        block_size = math.floor(math.sqrt(n))

        def get_key(x):
            # sort by:
            #   block that l belongs to
            #   then decreasing r if odd block, else increasing
            #   then l
            block = x[0] // block_size
            dec = block % 2
            return (block, -x[1] if dec else x[1], x[0])

        queries = sorted(
            [(l, r, i) for i, (l, r) in enumerate(queries)],
            key=get_key
        )

        w = Window(nums)
        ans = [False] * len(queries)

        for l, r, i in queries:
            r += 1
            while w.e != r:
                if w.e > r:
                    w.e -= 1
                    w.rem(w.e)
                else:
                    w.add(w.e)
                    w.e += 1
            while w.s != l:
                if w.s > l:
                    w.s -= 1
                    w.add(w.s)
                else:
                    w.rem(w.s)
                    w.s += 1
            ans[i] = (w.unq == k and w.odd == 0)

        return ans
