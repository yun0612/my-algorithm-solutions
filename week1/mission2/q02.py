"""
정수 리스트 nums와 목표값 target이 주어집니다. 리스트를 순회하며 target과 일치하는 모든 요소의 인덱스를 리스트에 담아 반환하세요. range(len(nums)) 대신 enumerate를 사용하여 구현해야 합니다.

예시)
    입력: nums = [1, 2, 3, 2, 1], target = 2
    출력: [1, 3]

TIP)
    enumerate() 함수는 리스트를 순환하면서 (인덱스, 값)을 동시에 반환합니다.
"""

def solution(nums, target):
    return [idx for idx, num in enumerate(nums) if num == target]

print(solution([1, 2, 3, 2, 1], 2))