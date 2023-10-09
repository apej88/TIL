## 날짜 출력
- 날짜와 시간을 출력하기 위해서
- datetime 모듈 import 
- from datetime import date, datetime
- date.today() : 오늘 날짜
- datetime.now() : 오늘 날짜 시간
- datetime.now().time() : 현재 시간

## 날짜 형식을 문자열로 변환 : strftime() 함수
- today.strftime(“%Y-%m_%d %H:%M:%S”)

## 문자열을 날짜 형식으로 변환 : strptime() 함수
- date = datetime.strptime(str_date, "%Y-%m-%d %H:%M:%S")