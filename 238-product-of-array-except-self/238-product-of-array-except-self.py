class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zCount = 0
        for i in nums:
            if i == 0: 
                zCount += 1
                continue
                
            mult *= i
        
        answer = []
        for i in nums:
            if i == 0 and zCount <= 1:
                answer.append(mult)
                continue
            if i != 0 and zCount > 0:
                answer.append(0)
                continue
            if i != 0 and zCount == 0:
                answer.append(mult//i)
                continue
            answer.append(0)

        return answer
