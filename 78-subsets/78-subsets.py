class Solution:
    def subsets(self, array: List[int]) -> List[List[int]]:

        def helper(arr, subsets):
            if len(arr) == 2: return
            for n in arr:
                newArr = slice(n, arr)
                subsets.add(newArr)
                helper(newArr, subsets)

        def slice(n, arr):
            return tuple(i for i in arr if i != n)
        
        if not array: return [array]
        if len(array) == 1: return [array, []]
        res = [[], array] + [[n] for n in array]
        subsets = set()
        helper(array, subsets)
        return res + list(subsets)