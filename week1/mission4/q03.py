"""
N명의 사람이 원으로 둘러앉아 있습니다 (1번~N번). 1번부터 시작하여 순서대로 K번째 사람을 제거합니다. 한 사람이 제거되면 남은 사람들끼리 원을 유지하며 이 과정을 반복합니다. 제거되는 사람들의 번호를 순서대로 담은 리스트를 반환하세요. (Deque의 rotate 활용 권장)

예시)
    입력: N = 7, K = 3
    출력: [3, 6, 2, 7, 5, 1, 4]
    (설명: 1, 2, 3 제거 -> 4, 5, 6 제거 -> 7, 1, 2 제거...)
"""

from collections import deque

def solution(n, k):
    result = []
    people = deque(range(1, n+1))

    while people:
        people.rotate(-(k-1))
        result.append(people.popleft())

    return result

print(solution(7, 3))