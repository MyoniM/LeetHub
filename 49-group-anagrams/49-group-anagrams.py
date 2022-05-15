class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        
        for s in strs:
            
            count = [0] * 26
            
            for c in s:
                # change the character to index (0 - 25)
                # ord("a") - ord("a") = 0
                count[ord(c) - ord("a")] += 1
                
            hashmap[tuple(count)].append(s)        
        
        return hashmap.values()