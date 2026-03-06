"""
문자열 리스트 strings와 정수 n이 주어질 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하세요. 만약 n번째 글자가 같다면, 사전순으로 앞선 문자열이 먼저 오도록 정렬하세요. (lambda 식 활용 필수)

예시)
    입력: strings = ["sun", "bed", "car"], n = 1
    출력: ["car", "bed", "sun"] ('a', 'e', 'u' 순서)

    입력: strings = ["abce", "abcd", "cdx"], n = 1
    출력: ["abcd", "abce", "cdx"] ('b'로 같으므로 사전순 정렬)
"""

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 1))