class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k: return '0'
        q = deque()
        for e in num:
            while q and q[-1] > e and k > 0:
                q.pop()
                k -= 1
            q.append(e)
        return str(int(''.join(q)[:len(q)-k]))