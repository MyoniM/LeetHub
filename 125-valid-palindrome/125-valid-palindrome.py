class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            while l < r and (not s[l].isalpha() and not s[l].isnumeric()): l += 1
            while r > l and (not s[r].isalpha() and not s[r].isnumeric()): r -= 1
            
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True