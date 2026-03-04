"""
정수로 이루어진 리스트 numbers가 주어집니다. 이 리스트에서 짝수만을 골라내고, 골라낸 값들을 제곱하여 새로운 리스트를 반환하는 함수를 작성하세요. (가능하면 for 반복문 대신 리스트 컴프리헨션을 사용해 한 줄로 구현해 보세요.)

예시)
    입력: numbers = [1, 2, 3, 4, 5, 6]
    출력: [4, 16, 36] (2의 제곱, 4의 제곱, 6의 제곱)

    입력: numbers = [1, 3, 5]
    출력: []
"""

def solution(numbers):
    return [n**2 for n in numbers if n % 2 == 0]

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 3, 5]))