# 크롤링
- 필요한 데이터가 있는 웹페이지의 구조를 분석하고 파악하여 긁어오는 것
## 필요 모듈
```python
from urllib.request import urlopen
import bs4
```
- 한 셀에서 여러 개의 결과값 출력
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
```
## 사이트 html
```python
url = '원하는 사이트'
html = urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')
# bs_obj에 원하는 사이트의 html을 불러온다
```

## find() 메소드
- find('태그명')
    - 태그명의 첫번째 데이터 반환
```python
bs_obj.find('div')
# <div>내용</div>
bs_obj.find('div').text
# 내용
```
- findAll('태그명')
    - 태그명의 모든 데이터 반환
```python
lis = ul.findAll('li')
for li in lis:
    print(li.text)
```
- 특정 속성을 가지고 있는 태그 추출
```python
find('태그명', {'속성명' : '속성값'})
find('ul', {'id' : 'title'})
```

## 형제 노드 찾기
- next_sibling
- find() 시 첫번재 데이터를 불러옴
- next_sibling을 이용하면 그 다음 데이터를 불러올 수 있음
```python
p = bs_obj.find('p')
p
p.next_sibling
p.next_sibling.next_sibling
```

## findAll()에서 원하는 태그 찾기
```python
# 첫번째 a 태그
bs_obj.findAll('a')[0]
# 두번째 a 태그
bs_obj.findAll('a')[1]
```

## 태그 내의 특정 속성의 값 추출
- find()한데이터.['속성값']
```python
# 첫번째 a 태그의 href 속성 값 추출
# [0]을 쓰지 않으면 오류
bs_obj_findAll('a')[0]['href']
```

## select() 메소드
- select('태그명')
    - 태그명의 모든 데이터 반환
```python
a_list = bs_obj.select('a')
for a in a_list:
    print(a.text)
# a 태그의 모든 text 출력
```
- css 선택자 사용 가능
    - 아이디 선택자 : #id명
    - 클래스 선택자 : .클래스명
    - 태그 선택자
        - 띄어 쓰기 : 자손 선택
        - '>' : 자식 선택
- select_one('태그명')
    - 1개의 태그 추출

# 데이터를 csv 파일로 저장
- 저장하고자 하는 데이터들을 리스트로 생성
- 데이터프레임 생성
- 파일로 저장
## (1) 섹션 메뉴와 링크를 리스트로 생성
- 빈 리스트 생성
```python
section = []
link = []
```
- 리스트에 추가
```python
lis = ul[0].findAll('li')
for li in lis:
    a_list = li.find('a')
    section.append(a_list.text)
    link.append(a_list['href'])
```

## (2) 데이터프레임 생성
```python
# 데이터프레임 생성 위해 모듈 임포트
import pandas as pd
# 열 이름과 리스트로 데이터프레임 저장
# pd.DataFrame({'Column name' : list, 'Column name' : list})
news_section_df = pd.DataFrame({'section' : section, 'link' : link})
```

## (3) 파일로 저장
- 데이터프레임.to_csv('파일경로 및 파일명', index=0)
```python
# 파일 저장
news_section_df.to_csv('./파일경로/파일명', index=0)
# 파일 로드
section_menu_df = pd.read_csv('./파일경로/파일명')
```