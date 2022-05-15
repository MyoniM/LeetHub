class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # loop through every element and check if it is is the map
        hashset = set()        
        for e in nums:
            if e in hashset: return True
            hashset.add(e)
        return False