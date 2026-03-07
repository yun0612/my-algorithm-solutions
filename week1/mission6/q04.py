"""
정수 리스트에서 홀수를 제거하려고 합니다. for 반복문으로 리스트를 순회하면서 직접 remove나 del을 할 때 발생하는 문제(인덱스 건너뜀)를 확인하고, 이를 해결하는 안전한 방법(새 리스트 생성 혹은 역순 순회 등)을 구현하세요.

예시)
    입력: numbers = [1, 2, 3, 4, 5]
    출력: [2, 4] (홀수가 모두 정상적으로 제거되어야 함)
"""

numbers = [1, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 1:
        numbers.remove(num)

print(numbers)  # [3, 4, 6]

# 리스트에서 원소를 제거하면, 뒤 요소들이 앞으로 당겨진다.
# 요소들은 앞으로 당겨졌지만 반복문의 인덱스는 그대로 다음 칸으로 이동한다.
# 즉, 앞으로 당겨지면서 의도치 않게 요소가 건너띄어진다.

# 안전한 방법1. 새 리스트 생성
numbers = [1, 3, 4, 5, 6]
result = []

for num in numbers:
    if num % 2 == 0:
        result.append(num)

print(result)

# 안전한 방법2. 역순 순회
numbers = [1, 3, 4, 5, 6]

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 1:
        numbers.remove(numbers[i])

print(numbers)

# 안전한 방법3. 리스트 컴프리헨션
numbers = [1, 3, 4, 5, 6]

result = [num for num in numbers if num % 2 == 0]

print(result)