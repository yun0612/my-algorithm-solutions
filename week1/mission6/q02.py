"""
문자열 리스트 strings가 있을 때, + 연산자로 합치는 것과 ''.join() 메서드를 사용하는 것의 성능 차이를 이해하고, 더 효율적인 방식(join)을 사용하는 함수를 작성하세요.

예시)
    입력: strings = ["Hello", " ", "World", "!"]
    출력: "Hello World!"
"""

import time

def bad_solution(strings):
    result = ""

    # `+`` 연산자 사용용
    start_time = time.time()
    
    for str in strings:
        result += str

    end_time = time.time()

    print(result)
    return (end_time - start_time) * 1000 # ms 단위로 반환

def good_solution(strings):
    # join() 메서드 활용
    start_time = time.time()

    result = " ".join(strings)

    end_time = time.time()

    print(result)
    return (end_time - start_time) * 1000

print(f"+ 연산자 사용 시간 : {bad_solution(["Hello", " ", "World", "!"])} ms")
print(f"join 함수 사용 시간 : {bad_solution(["Hello", " ", "World", "!"])} ms")