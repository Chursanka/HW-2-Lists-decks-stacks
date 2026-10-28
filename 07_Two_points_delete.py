def del_dup(arr):
    le = 0
    if (len(arr) > 1):
        while (le != len(arr) - 2):
            if arr[le + 1] == arr[le]:
                arr.pop(le + 1)
            else:
                le += 1
    return arr
