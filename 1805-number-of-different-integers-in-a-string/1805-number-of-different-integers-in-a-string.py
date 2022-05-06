class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for l in word:
            if l.isalpha(): word = word.replace(l,' ')
        unique_numbers = [int(i) for i in word.split()] 
        return len(set(unique_numbers))