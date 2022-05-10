class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return head 
        current = head
        to_be_next = None
        while True:
            temp_next =  current.next
            current.next = to_be_next
            to_be_next = current
            if not temp_next : break

            current = temp_next
        return current  
        
