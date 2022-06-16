class Solution(object):
    def findKthBit(self, n, k):
        ans=[]

        def invert(st):
            ans=''
            for x in st:
                if x=='0':
                    ans+='1'
                else:
                    ans+='0'
            return ans[::-1]
              
        def Recur(s,ans):
            if len(ans)==n:
                return  ans
            new=s+'1'+ invert(s)
            ans.append(new)
            Recur(new,ans)
            return ans[n-1][k-1]
            
        return Recur('0',[])