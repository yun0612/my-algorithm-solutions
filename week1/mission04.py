"""
정수 n이 주어질 때, 1부터 n까지의 모든 정수의 합을 구하여 반환하세요. for 반복문과 range() 함수를 반드시 사용해야 합니다.

예시)
    입력: n = 5
    출력: 15 (1 + 2 + 3 + 4 + 5)
"""

def solution(n):
    sum = 0

    for i in range(1, n+1):
        sum += i

    return sum

print(solution(5))