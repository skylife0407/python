s = "A man, a plan, a canal: Panama"
class test:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            
        while len(strs) >1:
            if strs.pop(0) != strs.pop():
                return False
            
        return True

t = test()
b = t.isPalindrome(s)
print(b)