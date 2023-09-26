def solution(data, col, row_begin, row_end):
    # 1. 
    row = sorted(data, key = lambda x: [x[col-1], -x[0]])
    # 2.
    ans = 0
    for i in range(row_begin, row_end+1):
        tmp = row[i-1]
        S_i = 0
        for j in tmp:
            a = j % i
            S_i += a
        ans ^= S_i
    return ans