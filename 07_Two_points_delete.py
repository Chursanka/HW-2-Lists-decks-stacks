def del_dup(arr):
    le = 0
    for ri in range(le+1, len(n) - 1):
        if arr[le] != arr[ri]:
            le += 1
            arr[le] = arr[ri]
    del arr[le + 1:]
    return arr
# le - правая граница уникальных символов, всё, что левее le - наш ответ. ri - необработанные элементы 
