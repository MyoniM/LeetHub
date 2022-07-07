class Solution:
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