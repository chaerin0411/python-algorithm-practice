''' 3-1.py 로그 파일 재정렬
    로그를 재정렬하라. 기준은 다음과 같다.
    1. 로그의 가장 앞 부분은 식별자다.
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
    4. 숫자 로그는 입력 순서대로 한다.
    풀이1 람다와 연산자를 이용 '''

'''
    입력
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    출력
    ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''

# 문자와 숫자를 구분하고, 숫자는 나중에 그대로 이어 붙인다.
# 로그 자체는 숫자 로그도 모두 문자열로 지정되어 있으므로, isdigit()을 이용해서 숫자 여부인지 판별
# 숫자로 변환 가능한 로그는 digits에, 그렇지 않은 경우 문자 로그는 letters에 추가
# 문자 로그는 letters에 모두 모였으므로 이를 정렬
# 식별자를 제외한 문자열 [1:]을 키로 하여 정렬
# 동일한 경우 후순위로 식별자 [0]를 지정해 정렬

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): # isdigit()을 이용하여 숫자인지 판별
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    # 식별자를 제외한 문자열 [1:]을 키로하여 정렬
    # 동일한 경우 후순위로 식별자 [0]를 지정해 정렬되도록, 람다 표현식을 이용해 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
