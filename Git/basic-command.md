# Basic Command

## 설정

- 커밋을 남기기 위해 사용자 정보를 입력하는 명령어
- 초기에 한번 작성

```bash
git config --global user.email <myemail>
git config --global user.name <myname>
```

## 명령어

`git init`
- 현재 폴더를 깃 폴더로 만들어줌
- 숨김 폴더 안에 .git 폴더가 생김

`rm -rf .git`
- 현재 폴더를 깃 폴더가 아니게 하는 방법
- rm : remove
- -r : 원래 rm 명령어는 폴더를 지울 수 없음 -r을 사용하면 폴더도 삭제
- f : 확실히 삭제해달라는 강제 명령어

`git add <파일 경로>`
- 변화된 파일 내용을 스테이징
- git add * 또는 git add . 을 입력하면 현재까지 발생된 변화된 내용을 스테이징
- 깃의 변화 감지는 어떤 걸 기준으로 할까? 
    - (1) git init 이후 변경된 내용을 기준으로 하는데
    - (2) 파일을 기준으로 함 (폴더만 있는 경우에는 변화를 인식 X)

`git status`
- 현재까지 스테이징에 올라와 있는 파일들을 확인

`git reset`
- 현재 스테이징 되어 있는 목록을 리셋

`git commit <커밋메시지>`
- 누가 커밋하는지에 대해서 이름이랑 email 설정 요청
- 메시지가 없으면 메시지 편집기로 들어감

`git log`
- 지금까지 커밋한 내용 확인

`git commit --amend`
- 편집기를 불러와 실수한 로그 수정