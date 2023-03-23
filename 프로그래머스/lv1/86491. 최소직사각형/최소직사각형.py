def solution(sizes):
    answer = 0
    short = []
    long = []
    for m, n in sizes:
        short.append(min(m, n))
        long.append(max(m, n))
    answer = max(short) * max(long)
    return answer