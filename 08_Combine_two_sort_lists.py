class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def combine_two_lists(head1, head2):
    node = ListNode(0)
    prev = node
    p1 = head1
    p2 = head2
    while (p1 != None) and (p2 != None):
        if p1.val > p2.val:
            prev.next = p2
            p2 = p2.next
        else:
            prev.next = p1
            p1 = p1.next
        prev = prev.next
    if p1 == None:
        prev.next = p2
    else:
        prev.next = p1
    return node.next
# Программа проходится по всем узлам двух списков один раз => Сложность O(n + m)
# Программа требует только один нулевой узел-заглушку на случай, если нужно будет вставить узел перед первым => O(1) по памяти
