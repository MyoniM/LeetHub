class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in words:
            key = self.getKey(word)
            anagrams[key] = anagrams.get(key, []) + [word]
        return list(anagrams.values())

    def getKey(self, word):
        alphabetArr = [0] * 26
        for c in word:
            order = ord(c) - ord('a')
            alphabetArr[order] += 1
        return tuple(alphabetArr)