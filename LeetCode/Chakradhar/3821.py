class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        z = 0
        m = 1
        while m < n:
            z += 1
            m = m * (k + z) // z

        ans = ['1']
        k -= 1
        cur = math.factorial(k+z) // (math.factorial(k) * math.factorial(z))
        n -= (m - cur)
        while k > 0 and z > 0:
            cur0 = (cur * z) // (k + z)
            if cur0 >= n:
                cur = cur0
                ans.append('0')
                z -= 1
            else:
                n -= cur0
                cur = (cur * k) // (k + z)
                ans.append('1')
                k -= 1

        while k > 0:
            ans.append('1')
            k -= 1
        while z > 0:
            ans.append('0')
            z -= 1

        return int(''.join(ans), 2)

