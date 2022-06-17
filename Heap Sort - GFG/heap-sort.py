#User function Template for python3

# O(nlog(n)) time | O(1) space
class Solution:
    def heapify(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else: 
                idxToSwap = childOneIdx
    
            if heap[idxToSwap] > heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
        
    def buildHeap(self,array, n):
        firstParentIdx = (n - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.heapify(currentIdx, n - 1, array)
         
    def HeapSort(self, array, n):
        self.buildHeap(array, n)
        for endIdx in reversed(range(1, n)):
            self.swap(0, endIdx, array)
            self.heapify(0, endIdx - 1, array)
            
    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends