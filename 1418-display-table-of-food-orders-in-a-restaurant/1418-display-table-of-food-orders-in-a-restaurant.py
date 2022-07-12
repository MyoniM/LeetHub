class Solution:
    def displayTable(self, o: List[List[str]]) -> List[List[str]]:
        r = [['Table']]
        fud, key = [], []
        d = {}
        f = {}
        for e in o:
            if e[2] not in f: fud.append(e[2])
            if e[1] not in f: key.append(e[1])
            f[e[2]] = 1
            f[e[1]] = 1

            if e[1] not in d:
                d[e[1]] = {}
            d[e[1]][e[2]] = d[e[1]].get(e[2],0) + 1

        fud.sort()
        key.sort(key = int)
        
        r[0] += fud
        for k in key:
            x = [k]
            for f in fud:
                x.append(str(d[k].get(f,0)))
            r.append(x)
        return r