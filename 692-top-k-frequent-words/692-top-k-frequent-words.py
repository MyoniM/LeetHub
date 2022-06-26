class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        
        result = []
        maxHeap = [(-freq[k], k) for k in freq.keys()]
        heapq.heapify(maxHeap)
        for _ in range(k):
            __, maxFreqWord = heapq.heappop(maxHeap)
            result.append(maxFreqWord)
        return result
            
    
        # if n is significantly greater than k,
        # then this approach would be slower since its time complexity is O(k*log(n))
        # so the approach below should be used
        
        # maxHeap = []
        # for key in freq.keys():
        #     heapq.heappush(maxHeap, (-freq[key], key))
        #     if len(maxHeap) > k:
        #         heapq.heappop(maxHeap)
        # return [el[1] for el in maxHeap]
    
        # this approach have O(n*log(k)) time complexity
        
        # both solutions have O(n) space complexity b/c of the hashmap