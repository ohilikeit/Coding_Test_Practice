def solution(genres, plays):
    res = []
    song = dict()
    sum_list = dict()
    n = len(genres)
    
    for i in range(n):
        genre = genres[i]
        play = plays[i]
        if genre in song:
            song[genre].append([i, play])
            song[genre].sort(key = lambda x: x[1], reverse=True)
        else:
            song[genre] = [[i, play]]
        if genre in sum_list:
            sum_list[genre] += play
        else:
            sum_list[genre] = play
    
    sorted_list = []
    for k in sum_list.keys():
        sorted_list.append([sum_list[k], k])
    sorted_list.sort(reverse=True)
    
    for i in sorted_list:
        for j in range(2):
            res.append(song[i[1]][j][0])
            if len(song[i[1]]) == 1:
                break

    return res