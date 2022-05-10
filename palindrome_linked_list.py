class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        values = []
        while current:
            values.append(current.val)
            current = current.next
        
        first = 0
        last = len(values)-1
        
        while first < last:
            if values[first] != values[last]: return False
            first+=1
            last-=1
        
        return True
        
