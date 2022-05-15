class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        nums = []
        ops = ["+","-", "*", "/"]
        
        for i in tokens:
            if i not in ops: nums.append(i)
            else:
                num1 = nums.pop()
                num2 = nums.pop()
                res = int(eval(str(num2) + i + str(num1)))
                nums.append(res)
                
        return nums[0]

        
