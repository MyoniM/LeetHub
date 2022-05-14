class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # sort the array
        piles.sort()
        
        l = len(piles)
        # calculate max loop
        partition = l // 3
        count = 0
        
        # example piles = [9,8,7,6,5,1,2,3,4]
        # sorted piles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # to get the max amount for us, we give bob all the smallest items => [1,2,3]
        
        # we are left with [4,5,6,7,8,9]
        # out of this, alice takes the max on every loop => [5,7,9]
        # we are left with [4,6,8]
        # this is the max we can get
        
        for i in range(partition,l,2):
            count+=piles[i]
        
        return count
