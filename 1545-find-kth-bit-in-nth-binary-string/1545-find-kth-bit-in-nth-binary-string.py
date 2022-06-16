
class Solution:
    def findKthBit(self, n, k):
        output = ''
        result = self.binary(n, output)
        return result[k-1]
    
    def binary(self, n, output):
        if n==1:
            output += "0"
            return output
        else:
            # saves it from computing twice
            x = self.binary(n-1, output)
            output += x + "1" + self.inverse(x)
            return output

    def inverse(self, bits):
        res = ''
        for i in bits:
            if i=="0":
                res+="1"
            else:
                res+="0"
        return res[::-1]
