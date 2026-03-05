"""
주어진 문자열 my_string을 스택(Stack) 자료구조의 특성(Last-In-First-Out)을 이용하여 뒤집은 문자열을 반환하는 함수를 작성하세요. 문자열을 순서대로 스택에 push한 뒤, 스택이 빌 때까지 pop하여 새로운 문자열을 만듭니다.

예시)
    입력: my_string = "Hello World"
    출력: "dlroW olleH"
"""

def solution(my_string):
    chars = [char for char in my_string]
    
    reversed = ""
    for i in range(len(chars)):
        reversed += chars.pop()
    
    return reversed

print(solution("Hello world"))