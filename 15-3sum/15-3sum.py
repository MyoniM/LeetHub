class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        a.sort()
        t = []
        n = len(a)

        for i,e in enumerate(a):
            if i > 0 and e == a[i - 1]:
                continue
            l, r = i + 1, n - 1
            x = -1 * e
            while l < r:
                s = a[l] + a[r]
                if s == x:
                    t.append([e, a[l], a[r]])
                    l += 1
                    while a[l] == a[l - 1] and l < r:
                        l += 1
                elif s > x: r -= 1
                else: l += 1
        return t