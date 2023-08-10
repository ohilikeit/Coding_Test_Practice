from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        ith_lst = []
        for order in orders:
            if len(order) >= i:
                ith_lst += [''.join(sorted(idx)) for idx in combinations(order, i)]
        order = Counter(ith_lst).most_common()
        
        if order != []:
            max_cnt = order[0][1]
            res = []
            if max_cnt >= 2:
                for i in order:
                    if i[1] == max_cnt:
                        res.append(i[0])
        answer += res

    return sorted(answer)

