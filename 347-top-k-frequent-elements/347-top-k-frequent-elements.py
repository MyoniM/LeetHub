class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time 
        if k == len(nums):
            return nums

        count = Counter(nums)
        mc = count.most_common(k)
        for i in range(len(mc)): mc[i] = mc[i][0]
        return mc