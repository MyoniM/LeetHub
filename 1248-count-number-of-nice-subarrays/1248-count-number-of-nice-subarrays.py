class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, n in enumerate(nums):
            if n % 2 == 0: nums[i] = 0
            else: nums[i] = 1
                
        ans = 0
        pSum = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1
        for n in nums:
            pSum += n
            diff = pSum - k
            ans += hashMap.get(diff, 0)
            hashMap[pSum] += 1
        return ans
