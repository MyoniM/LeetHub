class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        modulo = 10**9 + 7
        maxNum = pow(2, p, modulo)-1
        pairProduct = maxNum - 1
        pairCount = pow(2, p-1)-1
        return (pow(pairProduct, pairCount, modulo)*maxNum)%modulo