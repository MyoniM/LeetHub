class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bits = {"0": "1",
                "1": "0"}
        return self.getBit(n, bits)[k-1]
        
    def getBit(self, n: int, bits):
        if n == 1: return "0"
        bit = self.getBit(n - 1, bits)
        bitArr = []
        for b in bit:
            bitArr.append(bits[b])
            
        return bit + "1" + "".join(bitArr[::-1])