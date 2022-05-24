class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        if n == 1: return 1
        arr = list(range(1,n+1))
        
        def play(arr, i):
            l = len(arr)
            if l == 1: return arr[0]
            s = 0
            c = i
            while s < k:
                s+=1
                c=(c+1)%l

            arr.pop(c-1)
            return play(arr,(c-1)%l)
        
        return play(arr,0)