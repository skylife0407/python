from typing import List

s = ["h","e","l","l","o"]

# def reverseString(s:List[str])->None:
#     s.reverse()
#     print(s)

# reverseString(s)

def reverseString(s:List[str])->None:
    s=s[::-1]
    #s[:]=s[::-1]
    print(s)                                                   

reverseString(s)