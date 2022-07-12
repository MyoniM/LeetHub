class Solution:
    def search(self, n: List[int], t: int) -> int:
        l, r = 0, len(n) - 1
        while l <= r:
            i = (l + r)//2
            if n[i] == t: return i
            if n[l] <= n[i]:
                if t < n[i] and t >= n[l]: r = i -1
                else: l = i +1
            else:
                if t > n[i] and t <= n[r]: l = i +1
                else: r = i -1
        return - 1