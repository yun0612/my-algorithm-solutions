"""
리스트 data에는 시험 점수들이 들어있습니다. 가장 낮은 점수와 가장 높은 점수를 제외한 나머지 점수들의 평균을 구하기 위해, 언패킹(*)을 사용하여 min_score, mid_scores(리스트), max_score로 데이터를 분리하세요. (단, 데이터는 정렬되어 있다고 가정합니다.)

예시)
    입력: data = [50, 70, 80, 90, 100]
    결과: min=50, mid=[70, 80, 90], max=100

TIP)
    기본 언패킹
        - 변수와 원소의 개수가 동일해야 한다.
        - ex. `a, b, c = [1, 2, 3]`
    
    확장 언패킹
        - 변수에 하나씩 할당하고 *을 붙인 변수에 남은 원소를 리스트로 모아준다.
        - ex. `a, *b = [1, 2, 3]`
"""

def solution(data):
    min_score, *mid_scores, max_score = data
    return min_score, mid_scores, max_score

print(solution([50, 70, 80, 90, 100]))