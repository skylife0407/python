from typing import List

s = ["h","e","l","l","o"]
def reverseString(s:List[str]) ->None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -=1
    print(len(s))
    print(s)

reverseString(s)