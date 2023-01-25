from collections import defaultdict
def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    for i in records:
        time, car, state = i.split()
        time = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        dic[car].append(time)
    
    dic2 = defaultdict(list)
    for i in dic.keys():
        ans = 0
        # 출차 안되서 23시 59분 기준으로 계산 
        if len(dic[i]) % 2 != 0:
            dic[i].append(60 * 23 + 59)
        
        # 계산 
        total_time = 0
        for a in range(0, len(dic[i]), 2):
            total_time += (dic[i][a+1] - dic[i][a])
        if total_time <= fees[0]:
            ans = fees[1]
        else:
            idx = (total_time - fees[0]) // fees[2]
            if (total_time - fees[0]) % fees[2] == 0:
                ans = fees[1] + idx * fees[3]
            else:
                ans = fees[1] + (idx + 1) * fees[3]
        
        dic2[i] = ans
    
    for i in dic2.keys():
        answer.append((i, dic2[i]))
    answer.sort()
            
    return [i[1] for i in answer]