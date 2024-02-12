class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Ref: https://youtu.be/JoF0Z7nVSrA
        l1, l2 = len(haystack), len(needle)

        # Building the Longest Prefix-Suffix array of needle
        LPS = [0 for _ in range(l2)]
        p, c = 0, 1 # previous, current pointers
        # note: `p` is __kind of__ serving a dual purpose here,
        #        pointer as well as the length of matching pre-suf
        #        for current substr
        while c < l2:
            if needle[p] == needle[c]:
                LPS[c] = p + 1
                p, c = p + 1, c + 1
            else:
                if p == 0:
                    # 1st and last chars are not same (in needle[:c+1])
                    LPS[c] = 0
                    c += 1
                else:
                    p = LPS[p - 1]

        # Finding needle in haystack
        h, n = 0, 0 # haystack and needle pointers
        while h < l1:
            if haystack[h] == needle[n]:
                h, n = h + 1, n + 1
            else:
                if n == 0:
                    # nothing to gain from this substr
                    h += 1
                else:
                    # this is where the optimization happens, instead of resetting
                    # n = 0 & h = prevH+1 (brute-force), since previous char was 
                    # a match, reset it to the LPS at that point. I.e., we know
                    # the length of the prefix of already exhausted needle-substr 
                    # that is also its suffix, so we don't need to redo all that 
                    # computation and we slide the needle accordingly
                    n = LPS[n - 1]

            if n == l2: # reached end of needle, i.e., match found
                return h - l2

        return -1   # no match
