class Solution(object):
    def minSetSize(self, arr):
        count = Counter(arr)
        mc = count.most_common()
        s = 0
        removedCount = 0
        for i in mc:
            if removedCount >= len(arr) // 2:
                return s
            s += 1
            removedCount += i[1]
        return s