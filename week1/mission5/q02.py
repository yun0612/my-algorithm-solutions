"""
collections.Counter를 사용하여 다음 두 가지 기능을 구현하세요.
주어진 리스트에서 가장 많이 등장한 값(최빈값) 하나를 반환.
두 문자열 s1, s2가 주어질 때, 두 문자열의 구성 문자와 개수가 동일한 **애너그램(Anagram)**인지 판별(True/False).

예시)
    입력 1: [1, 2, 2, 3, 3, 3] -> 출력: 3
    입력 2: s1="listen", s2="silent" -> 출력: True
"""

from collections import Counter

def solution1(nums):
    return Counter(nums).most_common(1)[0][0]

def solution2(s1, s2):
    return Counter(s1) == Counter(s2)

print(solution1([1, 2, 2, 3, 3, 3]))

print(solution2("listen", "silent"))