class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        # arr len == 10
        # half == 5
        half = len(arr)//2
        count  = Counter(arr)
        
        # occurence freq with order  max -> min
        frequency = count.most_common()

        val = set_count = current_frequent_elem = 0
        
        while val < half:
            # get the item with max count
            max_item_count = frequency[current_frequent_elem][1]
            # add the count of the item to val
            val += max_item_count
            # increase our set count
            set_count+=1
            current_frequent_elem+=1
            
        return set_count
