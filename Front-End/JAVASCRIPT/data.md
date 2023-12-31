## 데이터 출력 방법
- alert(“출력 내용”)
    - window.alert() : window 생략하고 사용
    - “” 안의 내용을 알림창(경고창)으로 출력
- console.log(내용)
    - 개발자 도구의 console에 출력
- document.write(내용) - (연습용)
    - HTML 문서 (화면)에 내용 출력
- DOM (문서 객체 모델) 요소 사용

### 자바스크립트 코드 입력 시 주의점
- 대/소문자 구별
- 문장 끝에 세미콜론(;) 사용
- 괄호 짝이 맞아야 함
    - ( )
    - {  } : 중첩 사용 시 주의 
- 문자열에서 따옴표 겹침 오류 주의
    - document.write(“이름은 “홍길동” 입니다.”);
    - “  “  “    “ : 동일한 따옴표를 겹쳐 사용하면 오류
    - -> 작은따옴표 / 큰따옴표 구분해서 사용
    - “  ‘  ‘ ”
    - ‘   “  “  ‘
    - 특수문자 : \”
        - “    \”     \”    “

## 데이터 입력 방법
- confirm() 함수로 입력
- prompt() 함수로 입력  (연습용)
- < input > 태그의 value 속성 사용
- DOM 사용

### (1) confirm() 함수 
- 자바스크립트 내장 함수 : 그냥 사용하면 됨
- [확인]/[취소] 버튼이 있는 대화상자 출력
- [확인] 버튼을 누르면 true 반환
- [취소] 버튼을 누르면 false 반환


### (2) prompt() 함수로 입력 : 문법 연습용
- 자바스크립트 내장 함수
- 사용자로부터 입력 받은 값을 반환

## 자바스크립트에서 사용되는 데이터 타입 (값의 유형)
- 숫자 : 정수형, 실수형
- 문자 : ‘a’
- 문자열 : “string”, ‘작은 따옴표 사용 가능’
- 논리값 : true, false
- NaN : Not a Number (숫자가 아닌데 숫자로 사용할 경우)
- undefined와 null
    - null : 참조 객체 없음 의미 (값이 없을 때)
    - undefined : 값의 유형을 알 수 없음

### 데이터 타입 변환
- 문자열 “10”을 숫자 3으로 변환
- parseInt() : 정수값으로 형변환
    - “3” -> 3
- parseFloat() : 실수값으로 형변환
    - “3.14”  -> 3.14
- String() / toString() : 문자열로 형변환