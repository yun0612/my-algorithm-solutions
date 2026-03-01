"""
학생의 점수 score가 정수로 주어질 때, 다음 기준에 따라 학점을 문자열로 반환하는 함수를 작성하세요.
- 90점 이상: "A"
- 70점 이상 90점 미만: "B"
- 70점 미만: "C"

예시)
    입력: score = 85
    출력: "B"
"""

def solution(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

print(solution(85))