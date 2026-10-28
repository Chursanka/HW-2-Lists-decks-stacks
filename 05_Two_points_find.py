def two_sum (arr, target):
    if len(arr) < 2:
        return []
    l = 0
    r = len(arr) - 1
    while (l < r):
        s = arr[l] + arr[r]
        if s == target:
            return [l, r]
        else:
            if s > target:
                r -= 1
            else:
                l += 1
    return []
# В самом худшем случае цикл пройдет до середины массива => сложность O(n\2) = O(n)
