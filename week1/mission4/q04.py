"""
중요도가 담긴 문서 리스트 priorities가 주어집니다. 대기열의 가장 앞에 있는 문서를 꺼냈을 때, 나머지 대기열에 중요도가 더 높은 문서가 있다면 방금 꺼낸 문서를 대기열의 맨 뒤로 보냅니다. 그렇지 않다면 인쇄합니다. 내가 요청한 문서(인덱스 location)가 몇 번째로 인쇄되는지 구하세요.

예시)
    입력: priorities = [2, 1, 3, 2], location = 2 (값 3인 문서)
    출력: 1 (값 3인 문서가 가장 중요도가 높아 바로 인쇄됨)

    입력: priorities = [1, 1, 9, 1, 1, 1], location = 0
    출력: 5 (맨 앞의 1은 뒤로 밀리고, 9가 인쇄된 후 순서가 돌아옴)
"""
from collections import deque

def solution(priorities, location):
    requests = deque([(p, i) for i, p in enumerate(priorities)])
    print_count = 0
    
    while requests:
        current = requests.popleft()

        if any(current[0] < r[0] for r in requests):
            requests.append(current)
        else:
            print_count += 1
            if current[1] == location:
                return print_count

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))