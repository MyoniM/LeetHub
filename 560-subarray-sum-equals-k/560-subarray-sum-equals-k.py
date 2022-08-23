class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefixCount = {0:1}
        currentSum = 0
        
        for n in nums:
            currentSum += n
            kDiff = currentSum - k
            result += prefixCount.get(kDiff, 0)
            prefixCount[currentSum] = 1 + prefixCount.get(currentSum, 0)
            
        return result