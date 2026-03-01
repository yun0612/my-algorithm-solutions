"""
이름 name(문자열)과 나이 age(정수)가 주어질 때, f-string을 사용하여 "My name is [name] and I am [age] years old." 형식의 문자열을 반환하고, 별도로 name의 첫 번째 글자만 추출하여 반환하세요.

예시)
    입력: name="Alice", age=25
    출력: ("My name is Alice and I am 25 years old.", "A")
"""

def solution(name, age):
    return f"My name is {name} and I am {age} years old.", name[0]

print(solution("Alice", 25))
print(type(solution("Alice", 25)))  # <class 'tuple'>

"""
튜플로 반환되는 이유
: 파이썬에서는 `return`문에 쉼표로 연결된 값을 반환하면 인터프리터가 자동으로 하나의 튜플로 묶어서 반환한다.

튜플 특징
- 불변성 : 한 번 생성되면 내부 요소 수정, 삭제, 추가 불가
- 순서 보장 -> 인덱스 사용 가능
- 빠른 속도 : 고정된 크기 덕분에 조회 속도 빠름
- 다양한 자료형 : 하나의 튜플 안에 서로 다른 다양한 자료형 담을 수 있음
- 언패킹 가능 : 튜플의 요소를 변수에 각각 할당할 수 있음
    ```python
    intro, initial = solution("Alice", 25)
    print(intro)  # My name is Alice and I am 25 years old.
    print(initial)  # A
    ```
"""