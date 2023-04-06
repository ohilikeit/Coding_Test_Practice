from collections import defaultdict

def solution(genres, plays):
    res = []
    song = defaultdict(list)
    sum_list = defaultdict(int)
    n = len(genres)
    
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        
        song[genre].append([i, play])
        song[genre].sort(key = lambda x: x[1], reverse=True)
        
        sum_list[genre] += play

    sorted_list = []
    print(song)
    print(sum_list)
    print(sum_list.keys())
    # 속한 노래 많이 재생된 장르 먼저 수록을 위한 sort 
    for k in sum_list.keys():
        sorted_list.append([sum_list[k], k])
    print(sorted_list)
    sorted_list.sort(reverse=True)
    print(sorted_list)
    
    for i in sorted_list: # 속한 노래 기준으로 2개 넣고, 그 다음 장르 2개 넣고... 
        for j in range(2):
            res.append(song[i[1]][j][0]) # song[i[1]] : 장르명, [j][0] : 첫번째, 두번째 노래 
            if len(song[i[1]]) == 1:
                break # 장르에 속한 곡이 1개면 하나만 선택 

    return res