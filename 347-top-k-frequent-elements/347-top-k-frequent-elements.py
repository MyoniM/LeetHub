class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        mc = count.most_common(k)
        for i in range(len(mc)): mc[i] = mc[i][0]
        return mc