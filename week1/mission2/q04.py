"""
정수 n이 매개변수로 주어집니다. n이 0보다 크면 "Positive", 0이면 "Zero", 0보다 작으면 "Negative"를 반환하는 함수를 작성하세요. 일반적인 if-else 블록 대신, 한 줄로 표현 가능한 삼항 연산자(Ternary Operator) 형태를 중첩하여 작성해 보세요.

예시)
    입력: n = -5
    출력: "Negative"
"""

def solution(n):
    return "positive" if n > 0 else ("zero" if n == 0 else "negative")

print(solution(-5))