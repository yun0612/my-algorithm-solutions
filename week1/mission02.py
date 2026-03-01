"""
두 정수 num1, num2가 주어질 때, 두 수의 합, 차, 곱, 몫(정수 부분)을 순서대로 담은 리스트를 반환하고, 추가로 num1이 num2보다 큰지 여부(True/False)를 반환하는 함수를 각각 작성하세요.

예시)
    입력: num1 = 10, num2 = 3
    출력 1 (사칙연산): [13, 7, 30, 3]
    출력 2 (비교): True

"""

def solution1(num1, num2):
    return [num1 + num2, num1 - num2, num1 * num2, num1 // num2]

def solution2(num1, num2):
    return num1 > num2

print(solution1(10, 3))
print(solution2(10, 3))