"""
소괄호 (와 )로만 이루어진 문자열 s가 주어집니다. 괄호가 올바르게 열리고 닫혔는지 판별하여 True 또는 False를 반환하세요. 여는 괄호는 스택에 넣고, 닫는 괄호를 만나면 스택에서 꺼내 짝을 맞춥니다.

예시)
    입력: s = "(())()"
    출력: True

    입력: s = "(()("
    출력: False (닫히지 않은 괄호 존재)

    입력: s = ")()("
    출력: False (여는 괄호 없이 닫는 괄호 먼저 등장)
"""

def solution(s):
    result = []
    match = {")" : "("}

    for p in s:
        if p == "(":
            result.append(p)
        else:
            if not result:
                return False
            
            if match[p] != result.pop():
                return False
    
    return len(result) == 0

print(solution("(())()"))
print(solution("(()("))
print(solution(")()("))