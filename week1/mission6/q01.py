"""
100만 개의 데이터가 있는 리스트와 셋을 만들고, 특정 값이 존재하는지 확인하는 in 연산의 시간을 비교하는 코드를 작성하세요. (코드로 직접 성능 차이를 체감해 봅니다.)

TIP)
    time 모듈을 사요해 시작 시간과 종료 시간을 기록해서 차이 구하기
    - time 모듈 가져오기 : `import time`
    - 현재 시간 초 단위로 반환 : `time.time()`
"""

import time

def get_search_time(data, target):
    start_time = time.time()
    result = target in data
    end_time = time.time()

    return end_time - start_time

# 테스트 데이터 생성
data_list = list(range(1_000_000))   # 0 ~ 999999
data_set = set(data_list)            # 리스트 기반으로 set 생성

# 검색할 값 (존재하는 값 / 없는 값 둘 다 테스트 가능)
target_exist = 999_999
target_not_exist = 1_000_001

print("존재하는 데이터 검색-------------------")
print(f"리스트 검색 시간: {get_search_time(data_list, target_exist) * 1000} ms")
print(f"세트 검색 시간: {get_search_time(data_set, target_exist) * 1000} ms")

print("존재하지 않는는 데이터 검색-------------------")
print(f"리스트 검색 시간: {get_search_time(data_list, target_not_exist) * 1000} ms")
print(f"세트 검색 시간: {get_search_time(data_set, target_not_exist) * 1000} ms")