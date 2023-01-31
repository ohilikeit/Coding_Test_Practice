def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compress = ""
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                compress += str(count) + prev if count >= 2 else prev
                prev = s[i:i+step]
                count = 1
        compress += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compress))
        
    return answer