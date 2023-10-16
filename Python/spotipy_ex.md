## 아티스트명으로 앨범과 수록곡 정보 뽑아보기
### 필요 모듈 임포트
```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
```
### 검색할 아티스트와 빈 리스트 만들기
- '아이유' 검색
```python
artist = '아이유'
artist_search = sp.search(artist, type="artist")
ID = artist_search["artists"]["items"][0]["id"]
limits = 3
# 앨범 3개만 출력
album_search = sp.artist_albums(ID, limit=limits)

album_id = []
album_name = []
album_artist = []
album_image = []
album_release_date = []
artist_genres = artist_search['artists']['items'][0]['genres']
```
### 앨범 정보 저장
```python
for i in range(0, limits):
    album_id.append(album_search['items'][i]['id'])
    album_name.append(album_search['items'][i]['name'])
    album_artist.append(album_search['items'][i]['artists'][0]['name'])
    album_image.append(album_search['items'][i]['images'][0])
    # 이미지는 리스트 3개로 이미지 파일 크기가 다름
    album_release_date.append(album_search['items'][i]['release_date'])

for i in range(0,limits):
    print(f"앨범 아이디 : {album_id[i]}, 앨범 이름 : {album_name[i]}, 앨범 가수 : {album_artist[i]}, 앨범 발매일 : {album_release_date[i]}, 가수 장르 : {artist_genres}")
```
```
앨범 아이디 : 01dPJcwyht77brL4JQiR8R, 앨범 이름 : IU 5th Album 'LILAC', 앨범 가수 : IU, 앨범 발매일 : 2021-03-25, 가수 장르 : ['k-pop', 'pop']
앨범 아이디 : 5V8n6fqyAPxvFTibPhQVcp, 앨범 이름 : Palette, 앨범 가수 : IU, 앨범 발매일 : 2017-04-21, 가수 장르 : ['k-pop', 'pop']
앨범 아이디 : 56MqewtCUq5bplrqEYTVL0, 앨범 이름 : Modern Times – Epilogue, 앨범 가수 : IU, 앨범 발매일 : 2013-12-20, 가수 장르 : ['k-pop', 'pop']
```
### 앨범 수록곡 저장
```python
for i in range(0, limits):
    songs = sp.album_tracks(album_id=album_id[i])['items']
    print(f"앨범 아이디 : {album_id[i]}, 앨범 이름 : {album_name[i]}, 앨범 가수 : {album_artist[i]}, 앨범 발매일 : {album_release_date[i]}, 가수 장르 : {artist_genres}")
    for j in range(0, len(songs)):
        print(f"노래 id : {songs[j]['id']}, 노래제목 : {songs[j]['name']}, 가수 : {songs[j]['artists'][0]['name']}, 미리듣기 : {songs[j]['preview_url']}")
    print()
    print()
```
```
앨범 아이디 : 01dPJcwyht77brL4JQiR8R, 앨범 이름 : IU 5th Album 'LILAC', 앨범 가수 : IU, 앨범 발매일 : 2021-03-25, 가수 장르 : ['k-pop', 'pop']
앨범 아이디 : 5V8n6fqyAPxvFTibPhQVcp, 앨범 이름 : Palette, 앨범 가수 : IU, 앨범 발매일 : 2017-04-21, 가수 장르 : ['k-pop', 'pop']
앨범 아이디 : 56MqewtCUq5bplrqEYTVL0, 앨범 이름 : Modern Times – Epilogue, 앨범 가수 : IU, 앨범 발매일 : 2013-12-20, 가수 장르 : ['k-pop', 'pop']
앨범 아이디 : 01dPJcwyht77brL4JQiR8R, 앨범 이름 : IU 5th Album 'LILAC', 앨범 가수 : IU, 앨범 발매일 : 2021-03-25, 가수 장르 : ['k-pop', 'pop']
노래 id : 5xrtzzzikpG3BLbo4q1Yul, 노래제목 : LILAC, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/ccd524ffc8fe8f2e2972bfe2641a8347966da478?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 2j0MsDAMJ2ahsxP3z86ChI, 노래제목 : Flu, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/ad24b579230135a51d7010830e7bcf8d6ab00611?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 7CZRguMolNqIobnXxpV735, 노래제목 : Coin, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/76984dd3cc833134c0284618d7c33a5736681dcb?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 2M7a2Us8CEU1HZHj70byGX, 노래제목 : Hi spring Bye, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/578eec2f64ccfc339e29f5fd2de1e23c50cf714c?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 5nCwjUUsmBuNZKn9Xu10Os, 노래제목 : Celebrity, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/ab879698733f3b9ff65a70a4be0b60b92b94bb59?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 64P4md3mdMM8Dog2aThmzj, 노래제목 : Troll (Feat. DEAN), 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/772fe075b7ee11b439833eb551ed90557573cdfa?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 4YnVz2QRU6OnoJ8lt23QHM, 노래제목 : Empty Cup, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/21f1d9dc4399136a77bd373a62871af5098b142c?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 46wDG6evLn2iPoQ0F8CUWk, 노래제목 : My sea, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/afcec65fd4141486776365991647b2b4f4e22216?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 1IJxbEXfgiKuRx6oXMX87e, 노래제목 : Ah puh, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/9e48d81b0e2cf92217cb0915da903da2ef9ba2c7?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 6rcwrRWKyjaFyUL8b8GlIJ, 노래제목 : Epilogue, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/c39830f7dc5ebd1512e9bf79ec09058974a7074d?cid=c0ef6b3167de4affb312e7fc7366abb4


앨범 아이디 : 5V8n6fqyAPxvFTibPhQVcp, 앨범 이름 : Palette, 앨범 가수 : IU, 앨범 발매일 : 2017-04-21, 가수 장르 : ['k-pop', 'pop']
노래 id : 4NPARrLIbtMl29ZJv8ESr2, 노래제목 : dlwlrma, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/3d382100e48b3d1350c71ba63f14c0e550d52466?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 3y7ByLZ05tluscOTRgEJ9Y, 노래제목 : Palette (feat. G-DRAGON), 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/000dc56c20c8dd1e1baece8f70506185067e6723?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 06EMBzxDm2hueehobAlMtm, 노래제목 : Ending Scene, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/8b5075d9ecc3d622f2a6afaef550dc081d68c505?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 5MvxeZPiiLAuB5gI8k3ynk, 노래제목 : Can't Love You Anymore (With OHHYUK), 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/1410271308d98b4c4ae6b001b2525e78cc5e6f96?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 3h7WIL3B6nP3171zl6HWj8, 노래제목 : Jam Jam, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/861c655dbbbdff10056003b9ef9613497c52d0f2?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 1sUOFqmIU38dQCA13aVKBL, 노래제목 : Black Out, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/5ffcc10836e2ae8746bc214bb0f4c7f5eecaac4b?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 2HlvvNgav045pxmrG0mk11, 노래제목 : Full Stop, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/a4d0fe6677b96718d734ee3035de183e7d474044?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 3P3UA61WRQqwCXaoFOTENd, 노래제목 : Through the Night, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/31c4dc781b786be086f887a310e695085618ac4d?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 3dDJ4DlBQ0VaRYjLZhLDTa, 노래제목 : Love Alone, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/d7d3a477cdb79beac59a5afc92bd10dbf80973e7?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 1DP0uwV6tMlCEfR61Mh7ki, 노래제목 : Dear Name, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/d401603815dd6a62c7476c6976ed5f13f776bca0?cid=c0ef6b3167de4affb312e7fc7366abb4
...
노래 id : 13gJpKdOhieATKK3EaNDdz, 노래제목 : Wait, 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/9cc6efa7e5d987a1bde4168c9d3ff372f8f6bfc7?cid=c0ef6b3167de4affb312e7fc7366abb4
노래 id : 3KEVMEREcbQBAksOqlmyv8, 노래제목 : (Bonus Track) Voice Mail (Korean Version), 가수 : IU, 미리듣기 : https://p.scdn.co/mp3-preview/08f5d8013183e5bab8524dba64760d684d21f2b4?cid=c0ef6b3167de4affb312e7fc7366abb4


Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
50
앨범 아이디 : 01dPJcwyht77brL4JQiR8R, 앨범 이름 : IU 5th Album 'LILAC', 앨범 가수 : IU, 앨범 발매일 : 2021-03-25, 가수 장르 : ['k-pop', 'pop']
노래제목 : LILAC, 가수 : IU
노래제목 : Flu, 가수 : IU
노래제목 : Coin, 가수 : IU
노래제목 : Hi spring Bye, 가수 : IU
노래제목 : Celebrity, 가수 : IU
노래제목 : Troll (Feat. DEAN), 가수 : IU
노래제목 : Empty Cup, 가수 : IU
노래제목 : My sea, 가수 : IU
노래제목 : Ah puh, 가수 : IU
노래제목 : Epilogue, 가수 : IU


앨범 아이디 : 5V8n6fqyAPxvFTibPhQVcp, 앨범 이름 : Palette, 앨범 가수 : IU, 앨범 발매일 : 2017-04-21, 가수 장르 : ['k-pop', 'pop']
노래제목 : dlwlrma, 가수 : IU
노래제목 : Palette (feat. G-DRAGON), 가수 : IU
노래제목 : Ending Scene, 가수 : IU
노래제목 : Can't Love You Anymore (With OHHYUK), 가수 : IU
노래제목 : Jam Jam, 가수 : IU
노래제목 : Black Out, 가수 : IU
노래제목 : Full Stop, 가수 : IU
노래제목 : Through the Night, 가수 : IU
노래제목 : Love Alone, 가수 : IU
노래제목 : Dear Name, 가수 : IU
...
노래제목 : Hold my hand, 가수 : IU
노래제목 : Hold my hand (inst) (Instrumental), 가수 : IU


Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
앨범 아이디 : 79725WrSou2C9RrEUxClUf, 앨범 이름 : REAL+, 앨범 가수 : IU, 앨범 발매일 : 2011-02-17, 가수 장르 : ['k-pop', 'pop']
노래제목 : Only I didn't know, 가수 : IU
노래제목 : Scary Fairy Tale, 가수 : IU
노래제목 : Only I didn't know (With Pianist Kim Kwang Min), 가수 : IU


앨범 아이디 : 4WY1pPvmP9sBlVICuPxBQh, 앨범 이름 : REAL, 앨범 가수 : IU, 앨범 발매일 : 2010-12-09, 가수 장르 : ['k-pop', 'pop']
노래제목 : Not like this, 가수 : IU
노래제목 : What I'm doing slow, 가수 : IU
노래제목 : Good day, 가수 : IU
노래제목 : The night of the first breakup, 가수 : IU
노래제목 : In a room alone, 가수 : IU
노래제목 : Merry Christmas ahead (feat.Chundung), 가수 : IU
노래제목 : Good day (inst), 가수 : IU


앨범 아이디 : 6k40CO7zypyz3GqUxtaAiK, 앨범 이름 : Road No.1 OST Part.3, 앨범 가수 : IU, 앨범 발매일 : 2010-07-14, 가수 장르 : ['k-pop', 'pop']
노래제목 : Because I'm a Woman, 가수 : IU
노래제목 : Because I'm a Woman (PIANO VER.), 가수 : IU


앨범 아이디 : 5bB2nClfkdlG1ekRQGw8zT, 앨범 이름 : Nitpicking, 앨범 가수 : IU, 앨범 발매일 : 2010-06-03, 가수 장르 : ['k-pop', 'pop']
노래제목 : Nitpicking, 가수 : IU
노래제목 : Rain Drop, 가수 : IU
...
노래제목 : Tonight, 가수 : Yoon Hyun Sang
노래제목 : Everywhere in my room (Original Demo Ver.), 가수 : Yoon Hyun Sang


Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```
