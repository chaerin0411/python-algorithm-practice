''' 2-1.py 문자열 뒤집기
    문자열을 뒤집는 함수를 작성하라.
    입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
    풀이1 투 포인터를 이용한 스왑 '''

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

# 투 포인터는 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
# 점점 더 범위를 좁혀 가며 스왑하는 형태로 풀이
# '리턴 없이 리스트 내부를 직접 조작하라'는 제약 사항이 있으므로 s 내부를 스왑하는 형태로 풀이

def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1