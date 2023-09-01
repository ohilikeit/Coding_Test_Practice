def time_to_int(t):
    HH = int(t.split(':')[0])
    MM = int(t.split(':')[1])
    
    return HH * 60 + MM

def solution(book_time):
    imos = [0] * (24*60+10)
    for start, end in book_time:
        s, e = time_to_int(start), time_to_int(end)
        imos[s] += 1
        imos[e + 10] -= 1
    
    cummulative = 0
    max_ans = 0
    for i in range(24*60):
        cummulative += imos[i]
        max_ans = max(max_ans, cummulative)
    
    return max_ans