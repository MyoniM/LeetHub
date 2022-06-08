def has_cycle(head):
    if not head or not head.next: return 0
    first, second = head.next, head.next.next
    
    while first != second:
        if not first or not first.next: return 0
        if not second or not second.next: return 0
        first = first.next
        second = second.next.next
    
    return 1
