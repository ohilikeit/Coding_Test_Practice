def rotate_90(a):
    n = len(a)
    m = len(a[0])
    res =[[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = a[i][j]
    return res

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True 
    

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    
    # 새로운 자물쇠에 기존꺼 가운데에 채워넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 사방에서 돌면서 넣어보기 
    for rotate in range(4):
        key = rotate_90(key)
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠 채우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False





