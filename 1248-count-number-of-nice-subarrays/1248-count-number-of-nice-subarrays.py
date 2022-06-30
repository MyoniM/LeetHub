# O(n) time | O(n) space b/c of the hashmap

# you can find another variation of this problem here
# https://www.youtube.com/watch?v=fFVZt-6sgyo

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        pSum = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1
        for n in nums:
            pSum += 0 if n % 2 == 0 else 1
            diff = pSum - k
            ans += hashMap.get(diff, 0)
            hashMap[pSum] += 1
        return ans
