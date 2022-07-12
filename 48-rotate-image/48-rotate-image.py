class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(m) - 1
        for _ in range(len(m)//2):
            for j in range(r - l):
                t, b = l, r
                temp = m[t][l + j]
                m[t][l + j] = m[b - j][l]
                m[b - j][l] = m[b][r - j]
                m[b][r - j] = m[t + j][r]
                m[t + j][r] = temp
            l += 1
            r -= 1