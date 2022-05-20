class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        window = l = r = 0
        i_q = deque()
        d_q = deque()

        while r < len(nums):
            # get the max value from window
            while d_q and nums[d_q[-1]] <= nums[r]:
                d_q.pop()
            # get the min value from window
            while i_q and nums[i_q[-1]] >= nums[r]:
                i_q.pop()
                
            i_q.append(r)
            d_q.append(r)

            # subtract the min val from the max val
            # and shrink window
            # while it satisfies diff <= limit
            while nums[d_q[0]] - nums[i_q[0]] > limit:
                l+=1
                # pop the index in a queue when 
                # the left pointer becomes greater
                if l > i_q[0]: i_q.popleft()
                if l > d_q[0]: d_q.popleft()
            window = max(window, r-l+1)
            r+=1

        return window
            
            