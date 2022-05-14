class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # get len(m)
        # loop through len(m)
        # get sub array
        # sort
        # loop to check if arithmetic and store val in bool arr
        
        m = len(l)
        answer = [True]*m
        
        for i in range(m):
            start_index = l[i]
            end_index = r[i]
            
            sub_arr = nums[start_index:end_index+1]
            
            sub_arr.sort()
            
            diff = sub_arr[1] - sub_arr[0]
            
            for j in range(len(sub_arr)-1):
                if sub_arr[j + 1] -  sub_arr[j] != diff:
                    answer[i] = False
                    # extra loop not needed
                    break
                    
        return answer