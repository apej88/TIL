# VSCode에서 MongoDB 연동
- MongoDB for VS Code 확장팩 설치

- 연결 : Open form / Connect
- 왼쪽에서 나뭇잎 모양 클릭하면 데이터베이스 관리 화면으로 변경 
- [Create New Playground] 버튼 클릭
- 코드 입력 창 열고  코드 입력
- 우측의 실행 버튼 클릭하면 결과 창으로 결과 출력
---
## insert
- insert() : deprecated
- insertOne() : 한 개의 행 삽입
- insertMany() : 여러 행 삽입

## update
- update() : deprecated
- updateOne() : 한개의 행 수정
- updateMany() : 여러 행 수정
- upsert 파라미터
    - true : 조건에 해당되는 도큐먼트가 없는 경우 새로운 도큐먼트 insert
    - 기본 false : insert 하지 않음

## delete
- deleteOne()  : 하나의 도큐먼트 삭제
- deleteMany() : 여러 도큐먼트 삭제

# 쿼리 
- (1) 값으로 쿼리 
    - db.product({prdName:”텐트”})
- (2) 연산자를 이용한 쿼리
- 비교 연산자
- 논리 연산자
- 문자열 연산자
- 배열 연산자 
- 프로젝션 연산자

## (1) 비교 연산자
- $eq : 동일
- $ne : 비동일
- $gt : 초과
- $gte : 이상
- $lt : 미만
- $lte : 이하

## (2) : 논리 연산자
- $and
- $or
- $nor
- $not

## (3) 문자열 연산자
- $text
    - 문자열 검색 : 문자열 안에 포함되어 있는 문자열 검색
    - 검색하고자 하는 필드에 문자열 인덱스 설정해야 가능
        - bookName으로 검색하려면 bookName에 문자열 인덱스 생성
        - db.book.createIndex({bookName: ‘text’})
        - df.book.find({$text: {$search:”홍길동”}})
- $regex : 정규식으로 검색

## (4) 배열 연산자
- $all : 배열의 모든 요소 
- $elementMatch : 배열 안에서 조건에 맞는 요소 선택
- $size : 해당 배열의 크기와 크기가 같은 도큐먼트 선택