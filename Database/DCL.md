## DCL (데이터 제어어 : Data Control Language)
- 데이터의 사용 권한을 관리하는데 사용
- 권한 부여 및 취소

## 권한 (Privilege)
- 특정 유형의 SQL 문을 실행하거나 다른 사용자의 객체를 사용할 수 있는 권리

### 권한의 종류
- 시스템 권한
- 객체 권한

---
권한 부여 : GRANT 명령어 사용   
권한 제거 : REVOKE 명령어 사용

#### 객체 권한
- 특정 객체를 조작할 수 있는 권한
- 객체 : 데이터베이스, 테이블, 뷰 ...
- DML 사용 권한
    - SELECT
    - INSERT
    - UPDATE
    - DELETE

