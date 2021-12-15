import re

s = "A man, a plan, a canal: Panama"

def isPalindrome(s:str)->bool:
    s = s.lower()
    
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]','', s)
    # 영어 소문자, 숫자가 아닌 것은 ''로 치환
    #    => 영어 소문자, 숫자를 제외하고 나머지는 없앰.

    return s == s[::-1] # 슬라이싱
    # 전체를 거꾸로 가져와서 기존꺼랑 비교

print(isPalindrome(s))