# 선형 탐색 : 무작위로 늘여놓은 데이터 검색을 수행할 수 있다
# O(N)

# 배열에서 key와 같은 요소를 찾아 인덱스를 반환 index()

def seq_search(arr, key):
    i = 0
    while True:
        if i == len(arr): return -1
        if key == arr[i]: return i
        i += 1
    return i

# 보초법
# 두 가지 종료조건 중 종료조건 2번을 생략하는 방법

def seq_search_sen(arr, key):
    last_idx = len(arr) - 1
    if arr[last_idx] == key: return last_idx

    arr[last_idx] = key
    i = 0

    while True:
        if key == arr[i]:
            return -1 if i == last_idx else i
        i += 1