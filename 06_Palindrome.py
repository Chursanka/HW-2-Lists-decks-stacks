def is_palin(s):
    le = 0
    ri = len(s) - 1
    while (le != ri):
        if s[le] != s[ri]:
            break
        else:
            le += 1
            ri -= 1
    return le == ri
  # В самом худшем случае цикл пройдет до середины строки => сложность O(n\2) = O(n)
