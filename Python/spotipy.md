```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials(client_id=spt_id, client_secret=spt_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
```
## 빈 리스트 만들기
```python
artist_name =[]
track_name = []
track_popularity =[]
artist_id =[]
track_id =[]
for i in range(0,100,50):
    track_results = sp.search(q='year:2021', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        artist_id.append(t['artists'][0]['id'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        track_popularity.append(t['popularity'])
```

## 데이터프레임 만ㄷ르기
- pandas의 shape()함수 : 행과 열 개수 tuple로 반환
```python
import pandas as pd
track_df = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'track_popularity' : track_popularity, 'artist_id' : artist_id})
# print(track_df.shape)
track_df.head()
```
- 확인 훚
```python
artist_popularity = []
artist_genres = []
artist_followers =[]
for a_id in track_df.artist_id:
    artist = sp.artist(a_id)
    artist_popularity.append(artist['popularity'])
    artist_genres.append(artist['genres'])
    artist_followers.append(artist['followers']['total'])
```
- 데이터프레임 저장
```python
track_df = track_df.assign(artist_popularity=artist_popularity, artist_genres=artist_genres, artist_followers=artist_followers)
track_df.head()
```
## audio_features 뽑아내기
```python
track_features = []
for t_id in track_df['track_id']:
    af = sp.audio_features(t_id)
    track_features.append(af)

tf_df = pd.DataFrame(columns = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'])
```
- 확인하기
```python
for item in track_features:
    if item is not None and len(item) > 0:
        tf_df = pd.concat([tf_df, pd.DataFrame(item)], ignore_index=True)
tf_df.head()
```
## 전처리 작업
- url, 데이터 분석 필요없는 열 제거
```python
cols_to_drop2 = ['key','mode','type', 'uri','track_href','analysis_url']
tf_df = tf_df.drop(columns=cols_to_drop2)
print(track_df.info())
print(tf_df.info())
```
```python
track_df.sort_values(by=['track_popularity'], ascending=False)[['artist_name', 'track_name', 'track_popularity']].head(20)
```
