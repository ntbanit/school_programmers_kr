# https://school.programmers.co.kr/learn/courses/30/lessons/42579#
from collections import defaultdict
def solution(genres, plays):
    gc_times = defaultdict(int)
    gc_songs = defaultdict(list) # list of tuple (time_play, song_id) 
    for i in range(len(plays)) : 
        genre, time = genres[i], plays[i]
        gc_times[genre] += time
        gc_songs[genre].append((time, i))
    
    sort_gc_times = [] # list of tuple (time_play, genre_id)
    for genre in gc_songs :
        gc_songs[genre].sort(key = lambda x : (-x[0], x[1]))
        sort_gc_times.append((gc_times[genre], genre))
    
    sort_gc_times.sort(key = lambda x : (-x[0], x[1]))
    # print(gc_times)
    # print(sort_gc_times)
    
    answer = []
    for i in range(len(sort_gc_times)):
        genre = sort_gc_times[i][1]
        songs = gc_songs[genre]
        answer.append(songs[0][1])
        if len(songs) >= 2 :
            answer.append(songs[1][1])
    
    return answer