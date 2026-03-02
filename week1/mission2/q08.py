"""
문자열 s가 주어질 때, 짝수 번째 인덱스에 위치한 문자들만 모아서 새로운 문자열을 만드세요. 반복문 대신 슬라이싱의 세 번째 인자(step)를 활용하세요.

예시)
    입력: s = "abcdef"
    출력: "ace" (0, 2, 4번 인덱스)
"""

def solution(s):
    return s[::2]

print(solution("abcdef"))