def find_middle(head):
    left = head
    right = head
    while (right != null) or (right.next != null):
        right = right.next.next
        left = left.next
    return left

# right в два раза быстрее left "бежит" по списку => когда right пробежит n узлов, left пробежит n/2 (n/2 - 1/2 для нечетной длины)
