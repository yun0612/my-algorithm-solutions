"""
과목명이 담긴 리스트 subjects와 해당 과목의 점수가 담긴 리스트 scores가 주어집니다. for 문으로 하나씩 채워 넣는 방식 대신, zip 함수를 활용하여 {'과목명': 점수} 형태의 딕셔너리를 한 줄로 생성하세요.

예시)
    입력: subjects = ['Math', 'Sci'], scores = [90, 80]
    출력: {'Math': 90, 'Sci': 80}

TIP)
    zip() 함수는 두 개의 리스트를 하나의 튜플로 묶어서 반환합니다.
    단, 두 리스트의 길이가 다르면 짧은 리스트의 길이만큼만 묶습니다.
"""

def solution(subjects, scores):
    return dict(zip(subjects, scores))

print(solution(['Math', 'Sci'], [90, 80]))