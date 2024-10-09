class Solution:
    def isValid(self, code: str) -> bool:
        n = len(code)
        cdata = '[CDATA['
        stack = []
        l, r = 0, 0
        start_tag = False   # there needs to be atleast 1 of these
        while r < n:
            if code[r] != '<':  # TAG_CONTENT
                r += 1
                continue
            if (r == n - 1) or code[r+1] == '>':    # unmatched `<` or TAG_NAME is empty
                print(0)
                return False
            if code[r+1] == '/':    # end tag
                if len(stack) == 0:  # unmatched end tag
                    print(1)
                    return False
                pl, pr = stack.pop()
                tag_name = code[pl: pr]
                l, r = r + 2, r + 2
                while (r < n) and (code[r] != '>') and (code[r] == tag_name[r - l]):
                    r += 1
                if (r - l) != len(tag_name):
                    print(2)
                    return False
                if (r == n-1) and (pl != 1):
                    print(10)
                    return False
                l = r + 1
            elif code[r+1] == '!':  # CDATA
                l, r = r + 2, r + 2
                if (n - r) < 10:    # invalid CDATA
                    print(3)
                    return False
                while ((r - l) < 7) and (code[r] == cdata[r - l]):
                    r += 1
                if (r - l) < 7:
                    print(4)
                    return False
                while r < (n - 2) and not (code[r] == ']' and code[r+1] == ']' and code[r+2] == '>'):
                    r += 1
                if r == (n - 2):
                    print(5)
                    return False
                l = r + 1
            else:   # start tag
                start_tag = True
                l, r = r + 1, r + 1
                while (r < n) and code[r] != '>' and (65 <= ord(code[r]) <= 90) and ((r - l) < 9):
                    r += 1
                if r == n or code[r] != '>':
                    print(6)
                    return False
                stack.append((l, r))
                l = r + 1
            r += 1

        if start_tag and (len(stack) == 0) and (l >= r):
            return True
        else:
            print(7)
            return False
