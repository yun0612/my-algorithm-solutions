"""
빈 리스트를 생성하고, 숫자 1, 2, 3을 순서대로 추가(append)한 뒤, 최종 리스트의 길이(원소 개수)를 반환하는 함수를 작성하세요.

예시)
    입력: 없음
    출력: 3 (리스트 [1, 2, 3]의 길이)
"""

def solution():
    list = []

    list.append(1)
    list.append(2)
    list.append(3)

    return len(list)

print(solution())