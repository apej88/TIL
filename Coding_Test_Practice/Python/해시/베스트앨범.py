def solution(genres, plays):
    from collections import defaultdict  
    genre_to_plays = defaultdict(list)
    genre_total_plays = defaultdict(int)
    for i in range(len(genres)):
        genre_to_plays[genres[i]].append((plays[i], i))
        genre_total_plays[genres[i]] += plays[i]
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda x: genre_total_plays[x], reverse=True)
    answer = []
    for genre in sorted_genres:
        sorted_songs = sorted(genre_to_plays[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])
    return answer