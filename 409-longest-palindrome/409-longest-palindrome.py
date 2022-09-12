class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        f = 0
        ans = 0
        for k in count:
            c = count[k]
            if c % 2 == 0:
                ans += c
                f += 1
            else:
                ans += c - 1
        return ans if f == len(count) else ans + 1