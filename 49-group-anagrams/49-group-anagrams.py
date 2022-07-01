class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        # O(wn) time | O(wn) space
        # n being array length
        # w being length of the longest word
        anagrams = {}
        for word in words:
            key = frozenset(Counter(word).items())
            anagrams[key] = anagrams.get(key, []) + [word]
        return list(anagrams.values())