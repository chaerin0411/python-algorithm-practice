''' 1-3.py 유효한 팰린드롬
    주어진 문자열이 팰린드롬인지 확인하라.
    대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
    풀이3 슬라이싱 사용 '''

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
    s = s.lower()

    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱, 1-2.py의 데크 풀이 대비 2배 높은 속도
