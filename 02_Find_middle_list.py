def find_middle(head):
    left = head
    right = head
    while (right != None) and (right.next != None):
        right = right.next.next
        left = left.next
    return left

# right в два раза быстрее left "бежит" по списку => когда right пробежит до конца - left будет ровно на середине
