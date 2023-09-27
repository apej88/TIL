### 뷰 (View)
- 테이블의 일부를 추출하여 별도의 테이블로 생성한 가상 테이블
- 실제 데이터를 저장하는 것이 아니라 다른 테이블의 내용을 보여주는 역할 
- 다양한 형태의 뷰로 사용자에게 필요한 데이터 세트 제공
- 뷰를 통한 데이터 수정 및 삭제 가능 (단 접근 가능한 데이터만 변경 가능)
#### 뷰의 장점
- 보안성 : 사용자별로 접근 권한 다르게 뷰 생성
- 복잡한 쿼리 단순화
- 자주 사용되는 쿼리문을 뷰로 만들어 놓고 여러 번 사용

뷰 생성
```sql
CREATE VIEW client_view
AS
SELECT clientNo, clientName, clientAddress
FROM client;
```

뷰에서 데이터 조회 (테이블처럼 사용)
```sql
SELECT * FROM client_view;
```

뷰를 통해 데이터 변경 가능
```sql
-- (1) 뷰를 통해 INSERT 수행
-- 열이름 리스트 생략
INSERT INTO client_view VALUES('10', '케인', '제주');
-- 뷰를 통해 데이터를 insert 하면 원본 테이블의 데이터 변경
-- 즉, client 테이블에 데이터 추가되는데
-- clientNo, clientName, clientAddress 에만 값이 저장되고
-- 나머지 열은 null 값이 저장됨
-- NOT NULL로 설정되어 있는 열들이 포함되어 있어
-- NULL 허용으로 변경

-- 오류 : 뷰에 clientPhone 열은 포함되어 있지 않기 때문에 사용 불가
INSERT INTO client_view VALUES('10', '케인', '010-1111-1111', '제주');

-- (2) 뷰를 통해 update 수행
-- 고객번호 '1'의 주소를 '서울시'로 변경
UPDATE client_view SET clientAddress='서울시'  WHERE clientNo='1';
SELECT * FROM client;

-- (3) 뷰를 통해 delete 수행
-- 뷰를 통해 삽입한 데이터 삭제
DELETE FROM client_view WHERE clientNo='10';
```

뷰를 통해 삽입하지 않은 원래 있던 데이터도 삭제 가능
```sql
DELETE FROM client_view WHERE clientNo='9';
SELECT * FROM client_view;
```

뷰의 구조 변경 : ALTER 문 사용

```sql
ALTER VIEW client_view
AS
SELECT clientNo, clientName, clientAddress, clientHobby
FROM client;
```

