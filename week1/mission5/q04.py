"""
자연수 n이 주어졌을 때, 1부터 n까지의 모든 소수의 개수를 구하세요. 하나씩 소수인지 확인하는 방법 대신, 에라토스테네스의 체 알고리즘을 구현하여 효율적으로 구해야 합니다.

예시)
    입력: n = 10
    출력: 4 (2, 3, 5, 7 총 4개)
"""

def solution(n):
    sieve = [True] * (n + 1)    # 0 ~ n 까지 True 생성
    
    sieve[0] = sieve[1] = False # 0, 1 = 소수가 아님

    for i in range(2, int(n * 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):    # 배수 모두 False 처리
                sieve[j] = False
    
    return sum(sieve)

print(solution(10))