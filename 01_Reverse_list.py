def reverse_list(head):
    pred = null
    cur = head
    while (cur != nul):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    head = prev
    return head
