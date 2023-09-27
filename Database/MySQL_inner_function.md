### 수학 함수 
#### ROUND() 함수
- 반올림한 값을 구하는 함수
- ROUND(값, 자리수)
- 자리수 아래서 반올림하여 자리수까지 출력
    - 양수 값 : 소수점 오른쪽 자리수
        - 소수점 이하 자리수
    - 음수 값 : 소수점 왼쪽 자리수
        - 1의 자리, 10의 자리, 100의 자리


#### FORMAT() 
- 소수점 이하 자리수
천단위 구분 기호 표시 

- RANK() / DENSE_RANK() / ROW_NUMBER()

    - RANK() : 값의 순위 반환 (동일 순위 개수만큼 증가) 1 1 3 4 ...
    - DENSE_RANK() : 값의 순위 반환 (동일 순위 상관 없이 1 증가) 1 1 2 3 ...
    - ROW_NUMBER() : 행위 순위 반환. 1 2 3 ...

#### 문자 함수
- REPLACE() : 문자열을 치환하는 함수
    - REPLACE(전체문자열, 바꿀문자, 바뀐문자)
    - 테이블의 실제 데이터는 변경되지 않음

- CHAR_LENGTH()
글자의 수를 반환하는 함수

- LENGTH()
바이트 수 반환
    - UTF-8 : 한글 3 Byte, 스페이스 1 Byte

- SUBSTR()
지정한 길이만큼의 문자열을 반환하는 함수 
    - SUBSTR(전체문자열, 시작, 길이)

#### LOAD_FILE() 함수 
- 텍스트 파일의 내용
- 이미지 파일 : 이미지 저장
- 동영상 파일 : 동영상 저장
- 대용량 데이터 저장하기 위해 파일 로드 함수

- MySQL 시스템 변수 변경
    - 보안 
    - 디렉터리 접근 권한 설정 변경 
    - 파일 최대 크기 변수 변경
    - my.ini 파일에서 
    - max_allowed_packet=1024M
    - 수정/저장/MySQL 서버 재시작/워크벤치 재시작

- ini 파일 수정 
- 백업용으로 복사해 둘 것
- C:\ProgramData\MySQL\MySQL Server 8.0\my.ini
    - 이 위치에서 파일 열고 수정한 후 저장 안 됨 
- my.ini 파일을 메모장에서 열고 secure-file-priv 검색
- secure-file-priv="C:/dbWorkspace" 추가하고 저장
- 안됨 - 권한 없음
- my.ini 파일을 바탕화면으로 드래그한 후 수정/저장한 다음 원위치 
- 반드시 MySQL 서버 (서비스) 재시작 
- 워크벤치도 재시작

예제
```sql
CREATE TABLE flower(
	flowerNo VARCHAR(10) NOT NULL PRIMARY KEY,
    flowerName VARCHAR(30),
    flowerInfo LONGTEXT,
    flowerImage LONGBLOB
);

INSERT INTO flower VALUES('f005', '장미',
	LOAD_FILE('C:/dBWorkspace/rose.txt'),
    LOAD_FILE('C:/dBworkspace/rose.jpg'));

-- 파일 업로드/다운로드 경로 변수 확인
SHOW VARIABLES LIKE 'secure_file_priv';

-- 동영상 파일 저장
CREATE TABLE movie(
	movieId VARCHAR(10) NOT NULL PRIMARY KEY,
    movieTitle VARCHAR(50),
    movieDirector VARCHAR(20),
    movieStar VARCHAR(20),
    movieScript LONGTEXT,
    movieFilm LONGBLOB
);

INSERT INTO movie VALUES('1', '쉰들러 리스트', '스필버그', '리암 니슨',
	LOAD_FILE('C:/dbWorkspace/movies/Schindler.txt'),
    LOAD_FILE('C:/dBworkspace/movies/Schindler.mp4'));
```

#### 테이블 복사 구문 
- CREATE TABLE … AS SELECT
- 테이블 구조 + 데이터 모두 복사
- 형식
```sql
CREATE TABLE 새 테이블명 AS 
SELECT 복사할 열 FROM 원본 테이블명 [WHERE절]
```
- 주의!
    - 제약조건(기본키/외래키) 복사 안 됨
    - 복사 후 제약조건 설정해야 함