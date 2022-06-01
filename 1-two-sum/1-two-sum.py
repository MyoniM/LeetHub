class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            second = target - nums[i]
            if second in hashmap and hashmap[second] != i:
                return [i, hashmap[second]]