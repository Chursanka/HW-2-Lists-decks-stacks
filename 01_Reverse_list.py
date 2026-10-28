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

# Сложность O(n), так как программа один раз проходится по всем узлам списка
# prev - предыдущий узел 
# next - сохраненная ссылка на следующий узел
# cur - текущий узел
# До шага программы: prev -> cur  
# После шага программы: prev <- cur
