class Solution:
    def longestPalindrome(self, string: str) -> str:
        currentLongest = [0, 1]
        for idx in range(len(string)):
            odd = self.getLongestPalindrome(idx - 1, idx + 1, string)
            even = self.getLongestPalindrome(idx - 1, idx, string)
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            currentLongest = max(currentLongest, longest, key = lambda x: x[1] - x[0])
        return string[currentLongest[0]: currentLongest[1]]

    def getLongestPalindrome(self,leftIdx, rightIdx, string):
        while leftIdx >= 0 and rightIdx < len(string):
            if string[leftIdx] != string[rightIdx]:
                break
            leftIdx -= 1
            rightIdx += 1
        return [leftIdx + 1, rightIdx]