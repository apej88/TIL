1. 내장함수

- sum() : iterable 객체(List, Dict, Tuple 등)의 모든 원소의 합을 반환

```python
data = [1, 2, 3]
res = sum(data)
print(res)
>>> 6
```

- min() : 파라미터가 2개 이상 들어왔을 때 가장 작은 값 반환

```python
data = [1, 2, 3]
res = min(data)
print(res)
>>> 1
```

- max() : 파라미터가 2개 이상 들어왔을 때 가장 큰 값 반환

```python
data = [1, 2, 3]
res = max(data)
print(res)
>>> 3
```

- sorted() : iterable 객체가 들어왔을 때, 정렬된 결과를 반환

```python
data = [ 2, 4, 5, 6, 1, 2, 10, 0 ]

# ASC 정렬
sorted(data)
>>> [0, 1, 2, 2, 4, 5, 6, 10]

# DESC 정렬
sorted(data, reverse=True)
>>> [10, 6, 5, 4, 2, 2, 1, 0]

# List, Dict 정렬
data = [{"key":4},{"key":5},{"key":2},{"key":1},{"key":3}]
sorted(data, key=lambda x : x["key"])
>>> [{'key': 1}, {'key': 2}, {'key': 3}, {'key': 4}, {'key': 5}]

# List, Tuple 정렬
data = [("A", 4), ("B", 1), ("C", 3), ("D", 2), ("E", 5)]
sorted(data, key=lambda x : x[1])
>>> [('B', 1), ('D', 2), ('C', 3), ('A', 4), ('E', 5)]
```

2. itertools 함수

: 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

- permutations(순열) : iterable 객체에서 n 개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산

```python
from itertools import permutations

data = ["A", "B", "C"]
list(permutations(data, 3))
>>> [('A', 'B', 'C'),
 ('A', 'C', 'B'),
 ('B', 'A', 'C'),
 ('B', 'C', 'A'),
 ('C', 'A', 'B'),
 ('C', 'B', 'A')]
```

- combinations(조합) : iterable 객체에서 n 개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산

```python
from itertools import combinations

data = ["A", "B", "C"]
list(combinations(data, 3))
>>> [('A', 'B', 'C')]
```

- product(중복순열) : permutations 와 같이 iterable 객체에서 n 개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산(중복 허용)

```python
from itertools import product

data = ["A", "B", "C"]
list(product(data, repeat=3))
>>> [('A', 'A', 'A'),
 ('A', 'A', 'B'),
 ('A', 'A', 'C'),
 ('A', 'B', 'A'),
 ('A', 'B', 'B'),
 ('A', 'B', 'C'),
 ('A', 'C', 'A'),
 ('A', 'C', 'B'),
 ('A', 'C', 'C'),
 ('B', 'A', 'A'),
 ('B', 'A', 'B'),
 ('B', 'A', 'C'),
 ('B', 'B', 'A'),
 ('B', 'B', 'B'),
 ('B', 'B', 'C'),
 ('B', 'C', 'A'),
 ('B', 'C', 'B'),
 ('B', 'C', 'C'),
 ('C', 'A', 'A'),
 ('C', 'A', 'B'),
 ('C', 'A', 'C'),
 ('C', 'B', 'A'),
 ('C', 'B', 'B'),
 ('C', 'B', 'C'),
 ('C', 'C', 'A'),
 ('C', 'C', 'B'),
 ('C', 'C', 'C')]
```

- combinations_with_replacement(중복조합) : combinations와 같이 iterable 객체에서 n 개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산(중복 허용)

```python
from itertools import combinations_with_replacement

data = ["A", "B", "C"]
list(combinations_with_replacement(data, 3))
>>>[('A', 'A', 'A'),
 ('A', 'A', 'B'),
 ('A', 'A', 'C'),
 ('A', 'B', 'B'),
 ('A', 'B', 'C'),
 ('A', 'C', 'C'),
 ('B', 'B', 'B'),
 ('B', 'B', 'C'),
 ('B', 'C', 'C'),
 ('C', 'C', 'C')]
```

1. heapq

: 파이썬에서 힙 기능을 위해 heapq 라이브러리를 제공. heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용.

```python
import heapq

def heap_sort_asc(iterable):
    h = []
    res = []
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        res.append(heapq.heappop(h))
    
    return res

heap_sort_asc([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

1. bisect

: 파이썬에서 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공. “정렬된 배열”에서 특정한 원소를 찾아야할 때 매우 효과적으로 사용.

- bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드를 찾는 메서드(bisect(a, x) 와 동일)

```python
from bisect import bisect_left, bisect_right

data = [1, 2, 3, 4, 5, 5, 5, 6, 7]
target = 5
bisect_left(data, target)
>>> 4
bisect_right(data, target)
>>> 7
```

5. collections

: 파이썬의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리.

- deque : 보통 파이썬에서는 deque를 사용하여 큐 구현 가능하며, 인덱싱, 슬라이싱 등의 기능은 사용 불가. 또한 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때 매우 효과적.

```python
# popleft() : 첫 번째 원소 제거
# pop() : 마지막 원소 제거
# appendleft(x) : 첫 번째 인덱스에 원소 x를 삽입
# append(x) : 마지막 인덱스에 원소 x를 삽입

from collections import deque

data = deque([2,3,4])

data.appendleft("appendleft")
data.append("append")
print(data)
>>> deque(['appendleft', 2, 3, 4, 'append'])

data.popleft()
data.pop()
print(data)
>>> deque([2, 3, 4])
```

- Counter : iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 카운트 결과를 Dict 형태로 반환

```python
from collections import Counter

data = ["Apple", "Apple", "Apple", "Apple", "Apple", "Banna", "Banna", "Banna", "Banna", "Banna", "Melon", "Melon"]
counter = dict(Counter(data))
counter
```

6. math

: 자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리.

- factorial(x) : x! 값을 반환

```python
from math import factorial

factorial(3) # 1 x 2 x 3 = 6
>>> 6
```

- sqrt(x) : x의 제곱근 반환

```python
from math import sqrt

sqrt(4) # 루트 4
>>> 2.0
```

- gcd(a, b) : a 와 b의 최대공약수 반환

```python
from math import gcd

gcd(4, 2)
>>> 2
```

- lcm(a, b) : a 와 b의 최소공배수 반환

```python
from math import lcm

gcd(4, 2)
>>> 2
```

- 파이(pi), 자연상수(e)

```python
from math import pi, e

print("pi :", pi)
>>>pi : 3.141592653589793

print("e :", e)
>>>e : 2.718281828459045
```