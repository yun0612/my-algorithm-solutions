"""
정수 n이 주어졌을 때, 이 수가 소수(Prime Number)인지 판별하는 함수를 작성하세요. 2부터 n의 제곱근(sqrt(n))까지만 나누어 떨어지는지 확인하는 효율적인 방식을 사용해야 합니다.

예시)
    입력: n = 17 -> 출력: True
    입력: n = 20 -> 출력: False
"""
from math import sqrt

def solution(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

print(solution(17))
print(solution(20))