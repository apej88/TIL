## git branch

- 나무의 줄기. 여러 가지 뻗어나가는 다른 버전들의 묶음
- Commit에 이름을 붙여주고, 그 커밋부터는 별도의 버전으로 생각한다

```bash
# 브랜치 만들기
git branch 브랜치명
# git branch develop
```

```bash
# 브랜치 목록 확인하기
git branch
```

- 작업자 또는 작업하는 기능 단위로 현재 버전을 관리해줄 수 있는 기능
```bash
# 브랜치 삭제하기
git branch -d 삭제할 브랜치 이름 # 일반 삭제 (병합 후 삭제)
git branch -D 삭제할 브랜치 이름 # 강제 삭제 (병합되지 않는 경우) 
```

## git checkout

- develop 브랜치, main 브랜치 → 이 사이에 이동을 어떻게 해줄 것이냐
```bash
git checkout 이동할 브랜치 이름
```

- Switched to branch '…’ → 현재 이동한 브랜치 이름에 * 이 붙어 있는 걸 확인할 수 있음
```bash
# 이동할 브랜치를 만들고 바로 전환
git checkout -b 새로운 브랜치명
# 안 만들고 이동하면 path 오류가 남 (찾을 수 없다)
```

## 병합 시나리오

cake.txt

```
딸기케이크
```
```bash
git add .
git commit -m "레시피"
git checkout -b secret
```

- cake.txt를 만들고, 해당 내용을 커밋한 다음 그 커밋을 기준으로 secret 브랜치를 만든 것
```bash
git checkout -b secret2
# 브랜치를 전환하는 이유는, 새롭게 무언가를 시도하면서
# 커밋이나 추가된 파일이 내가 의도하지 않은 변화를 일으킬 수 있기에 따로 격리
```
- cake.txt
```
초코케이크
```
```bash
git add .
git commit -m "레시피2"
git checkout secret
git branch -d secret2 # merge를 하지 않았기 때문에 강제 삭제
```
```bash
git checkout -b secret3
```

- cake.txt
```
생크림케이크
```
```bash
git add .
git commit -m "레시피3"
git checkout secret # 원본이 되는 브랜치로 이동
git merge secret3 # 합치려는 브랜치 이름 제공
git branch -d secret3 # merge를 했기 때문에 강제 삭제할 필요 X
```

## git merge
```bash
git checkout {합침을 받으려는 브랜치명}
git merge {합치려는 브랜치명}
```

## 충돌 시나리오
```bash
git branch cat
git branch dog
# 현재의 기존 브랜치에서 cat과 dog으로 분화
git checkout dog
```

pet.txt
```
강아지
```
```bash
git add .
git commit -m "강아지"
git checkout cat
# cat의 버전에는 pet.txt가 없기 때문에 없는 취급
```

pet.txt
```
고양이
```
```bash
git add .
git commit -m "고양이"
git merge dog # cat 브랜치를 기준으로 dog 브랜치 병합
```
```bash
git merge --abort # 병합 취소
```
- 현재 변경 사항 : 현재 checkout되어 있는 branch의 사항을 적용
- 수신 변경 사항 수락 : merge를 통해 병합요청을 할 branch의 변경사항을 적용
- 두 변경사항 모두 수락 : 둘 다 적용
```bash
git add . # 변경사항을 결정한 다음에
git commit -m "병합 관련 메시지"
```