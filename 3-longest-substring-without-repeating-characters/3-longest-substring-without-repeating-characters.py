class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxLen = 0
        hashSet = set()
        
        while r < len(s):
            while r < len(s) and s[r] not in hashSet:
                hashSet.add(s[r])
                maxLen = max(maxLen, len(hashSet))
                r += 1
            hashSet.remove(s[l])
            l += 1
            
        return maxLen
