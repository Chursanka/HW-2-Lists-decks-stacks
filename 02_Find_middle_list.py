def find_middle(head):
    left = head
    right = head
    while (right != null) and (right.next != null):
        right = right.next.next
        left = left.next
    return left

# right в два раза быстрее left "бежит" по списку => когда right пробежит до конца - left будет ровно на середине
