''' 2-2.py 문자열 뒤집기
    문자열을 뒤집는 함수를 작성하라.
    입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
    풀이2 파이썬다운 방식 '''

'''
    입력
    ["h","e","l","l","o"]
    출력
    ["o","l","l","e","h"]

    입력
    ["H","a","n","n","a","h"]
    출력
    ["h","a","n","n","a","H"]
'''

# 입력값이 리스트로 제공되므로 reverse() 함수를 사용하여 뒤집기
# reverse()는 리스트에만 제공, 입력값이 문자열이라면 문자열 슬라이싱 사용

def reverseString(self, s: List[str]) -> None:
    s.reverse()
