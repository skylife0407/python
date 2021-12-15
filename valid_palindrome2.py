import collections
from typing import Deque


s = "A man, a plan, a canal: Panama"

class test:
    def isPalidrome(self, s:str) -> bool:
        strs: Deque = collections.deque
        # strs의 자료형을 데크로 선언

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                # popleft(): deque의 왼쪽에서 데이터를 반환하고 삭제
                return False
        
        return True

t = test()
print(t.isPalidrome(s))