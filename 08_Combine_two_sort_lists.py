class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def combine_two_lists(head1, head2):
    node = ListNode()
    node.next = head1
    prev = node
    p1 = head1
    p2 = head2
    while (p1 != null) and (p2 != null):
        if p1.val > p2.val:
            prev = p2
            next = p2.next
            p2.next = p1
            p2 = next
        else:
            prev = p1
            p1 = p1.next
    if p1 == null:
        while (p2 != null):
            p1.next = p2
            p2 = p2.next
        p1.next = null
       
    return node.next
# Программа проходится по всем узлам двух списков один раз => Сложность O(n + m)
# Программа требует только один нулевой узел-заглушку на случай, если нужно будет вставить узел перед первым => O(1) по памяти
