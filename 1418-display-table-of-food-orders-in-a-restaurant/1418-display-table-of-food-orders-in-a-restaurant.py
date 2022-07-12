class Solution:
    def displayTable(self, o: List[List[str]]) -> List[List[str]]:
        r = [['Table']]
        fud = set()
        d = {}
        for _, t, f in o:
            fud.add(f)
            if t not in d: d[t] = {}
            d[t][f] = d[t].get(f,0) + 1

        fud = list(fud)
        fud.sort()
        
        r[0] += fud
        for k in sorted(d, key = int):
            r.append([k] + [str(d[k].get(f,0)) for f in fud]) 
        return r