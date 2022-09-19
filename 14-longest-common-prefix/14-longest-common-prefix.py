class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = strs[0]
        for i in range(len(s1)):
            c = s1[i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or c != strs[j][i]:
                    return s1[0: i]
        return s1