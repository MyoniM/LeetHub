class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        length = len(word)
        count = 0
        for i, l in enumerate(word):
            if l in vowels:
                occurence = (length - i) * (i + 1)
                count += occurence
        return count
        