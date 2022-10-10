''' 1-2.py 유효한 팰린드롬
    주어진 문자열이 팰린드롬인지 확인하라.
    대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
    풀이2 데크 자료형을 이용한 최적화 '''

'''
    입력
    "A man, a plan, a canal: Panama"
    출력
    true

    입력
    "race a car"
    출력
    false
'''

def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    # 1-1.py의 리스트 풀이 대비 5배 높은 속도
    strs: Deque = collections.deque()
    
    for char in s:
        if char.isalnum(): # isalnum()는 영문자, 숫자 여부를 판별하는 함수
            strs.append(char.lower()) # lower()로 모두 소문자로 변환

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
