"""
여러 개의 단어가 담긴 리스트 words를 하나의 문장으로 합치려고 합니다. 반복문 내에서 + 연산자를 사용하여 문자열을 더하는 대신, join 메서드를 사용하여 단어 사이에 공백을 넣어 합치세요. (코딩 테스트에서 문자열 합치기 성능 최적화의 핵심입니다.)

예시)
    입력: words = ["Python", "is", "Easy"]
    출력: "Python is Easy"

TIP)
    join() 메서드는 리스트의 모든 요소를 하나의 문자열로 합쳐서 반환합니다.
    단, 리스트의 요소는 문자열이어야 합니다.
    + 연산자는 문자열 합치기 시 성능이 떨어지기 때문에 join() 메서드를 사용하는 것이 좋습니다.
"""

def solution(words):
    return " ".join(words)

print(solution(["Python", "is", "Easy"]))