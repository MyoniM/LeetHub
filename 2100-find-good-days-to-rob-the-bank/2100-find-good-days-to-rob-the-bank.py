class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        secLen = len(security)
        if time == 0: return [i for i in range(secLen)]
        if time > secLen // 2: return []
        
        nInc = [0] * secLen
        nDec = [0] * secLen
        for i in range(1, secLen):
            # ic
            if security[i] <= security[i - 1]:
                nInc[i] = nInc[i - 1] + 1
            # dec
            reverseIdx = secLen - i - 1
            if security[reverseIdx] <= security[reverseIdx + 1]:
                nDec[reverseIdx] = nDec[reverseIdx + 1] + 1
                
        res = []
        for i in range(time, secLen - time):
            if nInc[i] >= time and nDec[i] >= time:
                res.append(i)
        
        return res