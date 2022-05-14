# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left , right = 0, n
        
        while left <= right:
            num = left + (right - left) // 2
            if guess(num) == 0: return num
            elif guess(num) == 1: left = num +1
            else: right = num -1
            
        return -1