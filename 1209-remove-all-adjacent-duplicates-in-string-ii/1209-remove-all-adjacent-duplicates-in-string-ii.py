class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        result = ""
        for i in range(len(s)):
            result+=s[i]
            if len(result)>=k and s[i]*k == result[-1:-k-1:-1]: 
                result=result.replace(result[-1:-k-1:-1],"")
        return result