class Solution:
    def cyclicSort(self, s):
        n = len(s)
        s += s
        i, mn = 0, 0
        while i < n:
            mn = i
            j, k = i+1, i
            while (j < 2*n) and (s[k] <= s[j]):
                if s[k] < s[j]:
                    k = i
                else:
                    k += 1
                j += 1
            while i <= k:
                i += (j - k)
        return s[mn:mn+n]

    def minimumGroups(self, words: List[str]) -> int:
        d = defaultdict(int)
        for word in words:
            E, O = [] ,[]
            for i in range(len(word)):
                if i % 2:
                    O.append(word[i])
                else:
                    E.append(word[i])
            x = "".join(self.cyclicSort(E)) + "#" + "".join(self.cyclicSort(O))
            d[x] += 1

        return len(d)

