"""
문자열 s가 주어졌을 때, 각 문자가 몇 번 등장하는지 세어 {'문자': 등장횟수} 형태의 딕셔너리로 반환하세요. collections 모듈의 기능을 활용하면 더 간단하게 구현할 수 있습니다.

예시)
    입력: s = "banana"
    출력: {'b': 1, 'a': 3, 'n': 2}

    입력: s = "mississippi"
    출력: {'m': 1, 'i': 4, 's': 4, 'p': 2}
"""

from collections import Counter

def solution(s):
    return dict(Counter(s))

print(solution("banana"))
print(solution("mississippi"))