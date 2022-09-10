class Solution:
    def isInterleave(self, one: str, two: str, three: str) -> bool:
        

        def helper(ptr1, ptr2, one, two, three, cache):
            ptr3 = ptr1 + ptr2
            key = "{}-{}".format(ptr1, ptr2)
            if key in cache: return cache[key]
            if ptr3 == len(three): return True

            shouldInterweaveOne = True if ptr1 < len(one) and one[ptr1] == three[ptr3] else False
            shouldInterweaveTwo = True if ptr2 < len(two) and two[ptr2] == three[ptr3] else False
            if (shouldInterweaveOne or shouldInterweaveTwo) == False: return False

            validCombinationFound = False
            if shouldInterweaveOne:
                validCombinationFound = validCombinationFound or helper(ptr1 + 1, ptr2, one, two, three, cache)
            if shouldInterweaveTwo: 
                validCombinationFound = validCombinationFound or helper(ptr1, ptr2 + 1, one, two, three, cache)
            cache[key] = validCombinationFound
            return cache[key]

        if len(three) != len(one) + len(two): return False
        cache = {}
        return helper(0, 0, one, two, three, cache)

