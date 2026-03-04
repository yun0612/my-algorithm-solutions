"""
두 개의 정수 리스트 listA와 listB가 주어집니다. 두 리스트에 공통으로 포함된 숫자들만 찾아서 오름차순으로 정렬된 리스트를 반환하세요. (반복문을 사용한 O(N^2) 비교 대신 set 자료구조의 교집합 연산을 활용하세요.)

예시)
    입력: listA = [1, 5, 2, 3], listB = [2, 3, 4, 5, 9]
    출력: [2, 3, 5] (2, 3, 5가 양쪽에 모두 존재함)
"""

def solution(listA, listB):
    return sorted(list(set(listA) & set(listB)))

print(solution([1, 5, 2, 3], [2, 3, 4, 5, 9]))