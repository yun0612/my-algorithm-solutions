"""
문자열 s가 주어질 때, 해당 문자열에 모음(a, e, i, o, u)이 포함되어 있는지 여부를 판별하는 효율적인 코드를 작성하세요. 여러 번의 or 조건문 대신 in 연산자와 집합(Set)을 활용하여 파이썬스럽게 구현하세요.

예시)
    입력: s = "sky" → 출력: False
    입력: s = "apple" → 출력: True

TIP)
    (결과식 for 변수 in 반복대상)
        - 제너레이터 (...) : 계산하는 방법을 메모리에 저장하고 있을 뿐, 다른 메서드가 달라고 하기 전까지는 계산 X
        - `for 변수 in 반복대상`을 먼저 계산해서 결과식에서 사용할 변수 값을 준비하고, 준비된 변수를 꺼내서 결과식을 계산한다.
    
    any() : True가 발견되는 즉시 멈추고 True 반환 
"""

def solution(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return any(char in vowels for char in s)

print(solution("sky"))
print(solution("apple"))