class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        left = right = 0
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            diff = right - left
            chars[idx] = chars[left]
            idx += 1
            if diff > 1:
                for e in str(diff):
                    chars[idx] = e
                    idx += 1
            left = right
        return idx