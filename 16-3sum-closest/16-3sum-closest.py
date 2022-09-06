class Solution:
    def threeSumClosest(self, a: List[int], target: int) -> int:
        if len(a) == 3: return sum(a)
        a.sort()
        n = len(a)
        sm = (float('inf'), float('inf'))
        for i,e in enumerate(a):
            if i > 0 and a[i] == a[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                x = a[l] + a[r] + e
                if x == target:
                    return x
                if abs(x - target) < sm[0]:
                    sm = (abs(x - target), x)
                if x > target:
                    r -= 1
                elif x < target:
                    l += 1
        return sm[1]