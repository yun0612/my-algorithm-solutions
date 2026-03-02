"""
숫자 모양의 문자열이 담긴 리스트 str_nums를 정수형 리스트로 한 번에 변환하세요. for 루프를 사용하지 않고 map() 함수를 활용하여 구현해야 합니다.

예시)
    입력: str_nums = ["1", "2", "3"]
    출력: [1, 2, 3] (정수 리스트)

TIP)
    map(함수, 반복가능한 객체) : 반복 가능한 데이터의 각 요소에 함수를 적용해주는 함수 -> map 객체 반환
"""

def solution(str_nums):
    return list(map(int, str_nums))

print(solution(["1", "2", "3"]))