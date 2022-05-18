class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
                
        res=[]
        q = deque()
        l = r = 0
        
        # [1,3,-1,-3,5,3,6,7]
        
        while r < len(nums):
            #pop smaller values fromq
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
                
            if r + 1 >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res