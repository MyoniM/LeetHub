class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        NUM_MAP = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        answer = []
        comb = []
        def find(i):
            if i == len(digits):
                answer.append("".join(comb))
                return
            for j in NUM_MAP[digits[i]]:
                comb.append(j)
                find(i + 1)
                comb.pop()
                
        find(0)
        
        return answer