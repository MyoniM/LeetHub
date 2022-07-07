class Solution:
    # def findOriginalArray(self, changed: List[int]) -> List[int]:
        # return [] if len is odd
        # sort 
        # change to hash-map
        # check if i*2 exists for every item
#         changed.sort()
        
#         if len(changed) % 2 != 0: return []
        
#         # 6 3 0 1
        
#         hash_map = Counter(changed)
#         original_list = []
        
#         for item in changed:
#             if hash_map[item]:
#                 hash_map[item]-=1
#             else: continue
                
#             if  hash_map[item*2]: 
#                 original_list.append(item)
#                 hash_map[item*2]-=1

#         if len(original_list) * 2 == len(changed): return original_list
#         return []

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        res = []
        count = Counter(changed)
        for e in changed:
            if not count[e]: continue
            count[e] -= 1
            if count.get(e*2, 0) > 0:
                res.append(e)
                count[e*2] -= 1

        return res if len(res) == len(changed) / 2 else []