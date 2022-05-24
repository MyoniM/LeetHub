class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        if n == 1: return 1
        arr = list(range(1,n+1))
        
        # play takes players arr and starting index
        def play(arr, i):
            l = len(arr)
            # if only 1 player remains, return
            if l == 1: return arr[0]
            # step = (start index + k moves) % l
            # '%' b/c we dont want to go out of the boundary
            # -1 to get the index to pop
            step = ((i+k)%l) - 1
            arr.pop(step)
            # do the same thing after poping the element at step -1
            # continue from popped index + 1
            return play(arr,step%l)
        
        return play(arr,0)