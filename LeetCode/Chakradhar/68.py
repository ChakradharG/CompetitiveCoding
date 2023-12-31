class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        l, cur = 0, 0

        for r in range(len(words)):
            cur += len(words[r])
            gaps = r - l

            if (cur + gaps) < maxWidth:
                continue
            else:
                if (cur + gaps) > maxWidth:
                    cur -= len(words[r])
                    gaps -= 1
                    end, newCur = r, len(words[r])
                else:
                    end, newCur = r + 1, 0

                if gaps != 0:
                    numSpaces, rem = divmod(maxWidth - cur, gaps)
                else:
                    numSpaces, rem = maxWidth - cur, gaps

                s = ''
                for i in range(l, end):
                    s += words[i]
                    if i == l or i != end-1:
                        # handles both cases, don't add spaces after last word, and if this is the only word in this line, add all spaces to its right
                        s += ' ' * (numSpaces + ((i-l) < rem))
                ans.append(s)

                l = end
                cur = newCur

        if cur > 0:
            s = ''
            for i in range(l, r+1):
                s += (words[i] + ' ' * (i != r))
            s += (' ' * (maxWidth - len(s)))
            ans.append(s)

        return ans
