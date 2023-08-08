def counter(mat):
    base = mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != base:
                return False
    return True

def solution(arr):
    
    answer = []
    dic = {0:0, 1:0}
    
    def split_and_count(arr):
        n = len(arr) // 2
        # 더 이상 나눠지지 않으면 다 더해주고 끝내기
        if n == 1:
            for i in range(2):
                for j in range(2):
                    dic[arr[i][j]] += 1
            return dic
        
        a = [i[:n] for i in arr[:n]]
        b = [i[:n] for i in arr[n:]]
        c = [i[n:] for i in arr[:n]]
        d = [i[n:] for i in arr[n:]]

        for i in [a,b,c,d]:
            # 만약 하나의 원소로 이루어져있다면
            if counter(i):
                dic[i[0][0]] += 1
            # 조금이라도 다르다면 다시 분리하고 세어주기
            else:
                split_and_count(i)
                
    split_and_count(arr)
    if dic[0] == 0 and dic[1] % 4 == 0:
        return [0, 1]
    elif dic[1] == 0 and dic[0] % 4 == 0:
        return [1, 0]
    return [dic[0], dic[1]]