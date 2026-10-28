class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
  
def del_node(head, val):
    node = ListNode()
    node.next = head
    prev = node
    cur = head
    while (cur != null):
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return node.next 

# При удалении внутреннего узла мы "перепрыгиваем" через него 
# Для удаления первого узла, создаем нулевой узел, для того, чтобы можно было "перепрыгнуть" через первый
