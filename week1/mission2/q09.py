"""
단어 리스트 words가 주어집니다. 이 단어들을 단어의 길이를 기준으로 오름차순 정렬하세요. 길이가 같다면 사전순으로 정렬해야 합니다. sort 메서드의 key 인자에 lambda를 활용하세요.

예시)
    입력: words = ["apple", "no", "banana", "cat"]
    출력: ["no", "cat", "apple", "banana"]

TIP)
    `리스트.sort()` : 리스트 자체를 직접 정렬 -> None 반환
    `sorted(리스트)` : 원본 리스트는 건드리지 않고 정렬된 새로운 리스트 생성 및 반환

    파이썬은 튜플을 비교할 때 앞에서부터 비교한다.
    즉 (길이1, 단어1)과 (길이2, 단어2)를 비교할 때, 길이1과 길이2를 우선 비교한 후 길이가 동일하면 단어1과 단어2를 비교한다.
"""

def solution(words):
    # 방법1. 원본 리스트 정렬
    # words.sort(key=lambda x: (len(x), x))
    # return words

    # 방법2. 정렬된 새로운 리스트 반환
    return sorted(words, key=lambda x: (len(x), x))

print(solution(["apple", "no", "banana", "cat"]))