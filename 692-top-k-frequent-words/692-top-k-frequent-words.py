class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        
        # Solution 1 (Max Heaps) this approach have O(k*log(n)) time complexity

        # maxHeap = [(-freq[k], k) for k in freq.keys()]
        # heapq.heapify(maxHeap)
        # for _ in range(k):
        #     __, maxFreqWord = heapq.heappop(maxHeap)
        #     result.append(maxFreqWord)
        # return result
    
        # Solution 2 (Min Heaps) this approach have O(n*log(k)) time complexity
        
        # b/c we need to use min heaps for this solution
        # we need some way to compare the words if their frequency is equal
        # we cant use tuples for this as we will be needing the larger string first
        # we do that by creating a custom class (Word)
        class Word:
            def __init__(self, freq, word):
                self.word = word
                self.freq = freq
            def __lt__(self, other):
                # if two words have same frequency
                # we need the larger word to be at the top
                if self.freq == other.freq:
                    return self.word > other.word 
                return self.freq < other.freq

        minHeap = []
        for key in freq.keys():
            heapq.heappush(minHeap, Word(freq[key], key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        while minHeap:
            maxFreqWord = heapq.heappop(minHeap)
            result.append(maxFreqWord.word)
        return reversed(result)
        
        # both solutions have O(n) space complexity b/c of the hashmap
        # in worst case, all the elements could have frequency of 1, hence take O(n) space