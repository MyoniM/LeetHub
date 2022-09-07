class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1
        
        for coin in coins:
            for num in range(1, amount + 1):
                if coin > num: continue
                ways[num] += ways[num - coin]
        return ways[amount]