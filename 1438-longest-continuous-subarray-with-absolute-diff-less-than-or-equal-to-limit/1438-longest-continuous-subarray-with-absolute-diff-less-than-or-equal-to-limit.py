class Solution:
    def longestSubarray(self, ns: List[int], lm: int) -> int:
        lL = 0
        l, r = 0, 0
        n = len(ns)
        
        d_q = deque() # 10 1
        i_q = deque() # 1 

        # [10,1,2,4,7,2]
        while r < n:
            while d_q and ns[d_q[-1]] < ns[r]:
                d_q.pop()
            d_q.append(r)
            while i_q and ns[i_q[-1]] > ns[r]:
                i_q.pop()
            i_q.append(r)
            
            
            while ns[d_q[0]] - ns[i_q[0]] > lm:
                l += 1
                if i_q[0] < l: i_q.popleft()
                if d_q[0] < l: d_q.popleft()
            
            lL = max(r - l + 1, lL)
            
            r += 1

        return lL