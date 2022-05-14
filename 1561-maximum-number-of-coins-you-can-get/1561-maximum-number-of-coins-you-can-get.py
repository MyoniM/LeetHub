class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # sort the array
        piles.sort()
        # calculate max loop
        partition = len(piles) // 3
        count = 0
        
        # to icrease maximum number of coins that you can have
        # give Bob the 0 element, alice the -1 elem and the -2 elem for yourself
        for i in range(partition):
            # [min, max, second max]
            # add the second max to count
            # O(n), O(1), O(1)
            sub_arr = [piles.pop(0),piles.pop(len(piles)-1), piles.pop(len(piles)-1)]
            count += sub_arr[2]
                
        return count