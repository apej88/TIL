파이썬 코테 준비
1. 기본 기능
- 문자열 뒤집기
```python
string[::-1]
```
- 중복 제거
```python
temp = list(set(temp))
```
- 여러 수 받기
```python
temp_list = list(map(int, input().split()))
```
- 특정 값 2차원 맵
```python
visted = [[False for _ in range(m)] for _ in range(n)] # n: 행 개수 m: 열 개수 (BFS, DFS 등에서 주로 활용)
```
- if 0 < n < 10: 허용
- 변수 값 바꾸기
```python
a, b = b, a
```
- 리스트 인덱스, 값 가져오기
```python
for idx, value
```
- Queue 사용시
temp.pop(0)대신 deque사용
```python
from collection import deque
queue = deque([1, 2, 3, 4, 5])
idx0 = queue.popleft() # appendleft()도 사용 가능
- 길이가 같은 2개 이상의 iterable 객체 동시 for문
for n1, n2 in zip(temp1, temp2):
	print(n1, n2)
```
- 딕셔너리 정렬 (key, value 각 기준)
```python
# key 기준
sorted(dic.item(), key = lambda x: x[1])
# value 기준
sorted(dic.item(), key = lambda x: (x[1], x[0]))
```
- 정렬된 리스트에서 이진 탐색으로 탐색 및 값 삽입하기
```python
import bisect
lst = [1, 3, 5, 6, 6, 8]
print(bisect.bisect_left(lst, 4)) # 2
# bisect_left는 그 숫자의 가장 왼쪽 index 반환
# bisect_right는 그 숫자의 가장 오른쪽 index 반환
- 2차원 리스트에서 열 추출하기
# zip 연산을 통해 간단히 구현
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = list(zip(*a))[0]
print(b) # (1, 4, 7)
```
- 표준 입력으로 시간 단축하기
```python
import sys
input sys.stdin.readline
while True:
	num = int(input())
	if num == -1: break
	print(num)
```
- defaultdict() 유사 딕셔너리
```python
if 1 in dic:
	dic[1].append('temp')
else:
	dic[1] = 'temp'
# key가 존재하지 않으면 에러가 발생한다. 이때, defaultdict() 사용
from collections import defaultdict
dic = defaultdict(list)

N = int(input())

for i in range(N):
    deadline, cup = map(int, input().split())
    dic[deadline].append(cup)
```
- 우선순위 큐
```python
# heap은 push, pop 모두 O(logN)이 소요된다
import heapq

priority_queue = []

for idx, val in enumerate([3, 1, 9, 24, 13, 71]):
    heapq.heappush(priority_queue, (val, f'작업{idx + 1}'))

    # 우선순위가 가장 낮은 요소부터 우선순위 큐에서 제거하고 출력 (최소 힙)
while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f'우선순위: {priority}, 작업: {task}')

# 만약 우선순위가 가장 높은 요소부터 추출하려면? (최대 힙)
priority_queue = []

for idx, val in enumerate([3, 1, 9, 24, 13, 71]):
    heapq.heappush(priority_queue, (-val, f'작업{idx + 1}'))  # 우선순위에 -를 곱해서 넣으세요!

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f'우선순위: {priority}, 작업: {task}')
```
- 2차원 리스트 깊은복사
```python
# 파이썬 [:] 연산은 첫 번째 차원은 깊은 복사이지만, 내부 배열은 참조 유지
# deepcopy() 사용해야 새로운 메모리 위치에 복사하여 독립적 복사본 생성
import copy

# 2차원 배열 생성
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 얕은 복사
shallow_copied = original[:]
shallow_copied[0][0] = 999
print("얕은 복사 후 원본 배열:", original)  # 변경됨!

# 깊은 복사
deep_copied = copy.deepcopy(original)
deep_copied[0][0] = 111
print("깊은 복사 후 원본 배열:", original)  # 변경되지 않음!
print("깊은 복사된 배열:", deep_copied)
```