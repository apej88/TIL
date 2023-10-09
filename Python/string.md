# 문자열 (String)
- 문자의 나열
- 작은 따옴표, 큰 따옴표 모두 사용 가능

## 문자열 연결 : + 연산자 사용
- 문자열 + 문자열
- 주의 
    - 문자열과 숫자 연결 시 형변환 필요
    - 문자열 + str(숫자) + 문자열

## 문자열 곱하기
- 곱하는 수만큼 반복
- string = “파이썬”
- result = string * 3
- 파이썬파이썬파이썬

## 문자열 인덱싱 (indexing)
- 인덱스로 문자의 위치를 나나태는 것
- 인덱스 : 문자의 위치. 0부터 시작
- string[0] : 인덱스 0번째 문자 (첫 번째 문자)
- string[-1] : 마지막 문자

## 슬라이싱 (slicing)
- 문자열 중에서 일부분을 추출하는 것 (잘라내는 것)
- n인덱스 사용
- string[n] : 인덱스 n번째 문자 
- string[0:n] : 0부터 n-1번째까지의 문자열 
- string[n:] : n부터 끝까지
- string[:n] : 0부터 n-1까지
- string[-1:] : 마지막 문자 (마지막에서 끝까지)
- string[:-1] : 처음부터 마지막-1까지
- string[:] : 전체 문자열

## in / not in
- 문자열에 특정 문자열이 포함되어 있는지 여부 확인
- 결과는 True, False

## 문자열 관련 메소드 (함수)
### len() : 함수
- 문자열의 길이 반환
- print(len(string))

### count()
- 문자열 내에 들어 있는 특정 문자(열)의 개수 반환
- string.count(“a”)  # 2

### find()
- 문자열 내에서 특정 문자열이 존재하는지 여부와 문자열의 시작 위치를 반환
- 존재하지 않으면 -1 반환
- 필요한 문자열만 추출할 수 있도록 필터링 하거나 검사할 때 주로 사용
- crawling = “Data crawling is fun”
- print(crawling.find(“fun”))	# 17
- print(crawling.find(“f”))		# 17
- print(crawling.find(“parsing”))	# -1 (없음)

### index()
- 문자열 내에서 특정 문자열의 시작 위치를 반환
- 없으면 오류

### split()
- 구분자를 기준으로 문자열을 분리
- 리스트로 반환
- 구분자 : 기본은 공백
- 구분자 지정 : “-”, “:”, “,”, …

### replace()
- 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경
- 전체문자열.replace(찾는 문자열, 변경할 문자열)
- 찾는 문자열이 존재하면 변경된 문자열 반환
- 찾는 문자열이 존재하지 않는 경우 변경된 내용이 없기 때문에 원래 문자열 반환

### join()
- 각 문자 사이에 특정 문자(열) 삽입
- a =“aa”
- a.join(“bbb”)
- a를 b 사이에 삽입
- 결과 : baabaab
- 문자열 사이에 구분자 삽입 시 사용
    - a = "-"
    - print(a.join("abcd"))
    - 결과 : a-b-c-d

### upper() / lower() / capitalize() / title()
- upper()
    - 소문자를 대문자로 변환
- lower()
    - 대문자를 소문자로 변환
- capitalize()
    - 문장의 첫 번째 문자를 대문자로 변환
- title() 
    - 각 단어의 첫 글자를 대문자로 변경

### strip() / lstrip() / rstrip()
- strip()
    - 문자열 앞 뒤의 공백 제거 (양쪽 다 제거)
- lstrip()
    - 문자열의 왼쪽 공백 제거
- rstrip()
    - 문자열의 오른쪽 공백 제거

### isalpha() / isdigit() / isspace() / isalnum()
- 문자/숫자/공백 여부 확인 메소드
- 결과 : True, False 반환
- isalpha()
    - 문자 여부 결과 반환 (True, False)
- isdigit()
    - 숫자 여부 결과 반환 (True, False)
- isspace()
    - 하나의 문자에 대해 공백 여부 결과 반환 (True, False)
- isalnum()
    - 문자 또는 숫자 여부 결과 반환 (True, False)

## 문자열 포맷팅 
### 포맷팅 방법
- 포맷 코드 사용 : %s, %d, %f, %c
- format() 함수 사용
    - print(“당신의 BMI”, format(bmi, ‘.2f’))
- 문자열 포맷팅 : 문자열.format()
    - print(“{0}”.format(name))
    - print(“{name} “).format(name=”홍길동”)
- f-string 사용
    - print(f”문자열 {변수})
    - 문자열 정렬도 가능

## 문자열 정렬 : 정렬 문자 사용 (<, >, ^)
- 왼쪽 정렬 : <
    - “{0:<10}”.format() : 전체 10자리 왼쪽 정렬
- 오른쪽 정렬 : >
    - “{0:>10}”.format() : 전체 10자리 오른쪽 정렬
- 가운데 정렬 : ^
    - “{0:^10}”.format() : 전체 10자리 가운데 정렬
- 공백문자 지정 : -로 지정 시 (공백대신 -로 출력)
    - “{0:-^10}”.format()