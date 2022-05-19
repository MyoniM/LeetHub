class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)

        for i, e in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < e:
                prev_i = stack.pop()
                ans[prev_i] = i - prev_i
                
            stack.append(i)
        return ans