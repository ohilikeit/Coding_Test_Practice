import re 
from collections import defaultdict


def solution(record):
    answer = []
    id_list = {i.split()[1] : i.split()[2] for i in record if i.split()[0] != 'Leave'}
    
    for i in record:
        idx = i.split()
        if idx[0] == 'Enter':
            answer.append(id_list[idx[1]] + '님이 들어왔습니다.')
        if idx[0] == 'Leave':
            answer.append(id_list[idx[1]] + '님이 나갔습니다.')
        
    return answer