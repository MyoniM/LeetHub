class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = 0
        maxFruits = 0
        hashSet = {}
        
        while r < len(fruits):
            if len(hashSet) == 2 and fruits[r] not in hashSet:
                minVal = float('inf')
                for val in hashSet.values():
                    minVal = min(minVal, val)
                key = fruits[minVal]
                l = hashSet[key] + 1
                del hashSet[key]                
                continue
                
            hashSet[fruits[r]] = r
            r += 1
            maxFruits = max(maxFruits, r - l)
            
        return maxFruits