def rotate(matrix, query):
    x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
    prev = matrix[x1][y1]
    smallest = prev
    
    # 위쪽 테두리
    for i in range(y1+1, y2+1):
        matrix[x1][i], prev = prev, matrix[x1][i]
        smallest = min(smallest, prev)
    
    # 오른쪽 테두리
    for i in range(x1+1, x2+1):
        matrix[i][y2], prev = prev, matrix[i][y2]
        smallest = min(smallest, prev)
    
    # 아래쪽 테두리
    for i in range(y2-1, y1-1, -1):
        matrix[x2][i], prev = prev, matrix[x2][i]
        smallest = min(smallest, prev)
    
    # 왼쪽 테두리
    for i in range(x2-1, x1-1, -1):
        matrix[i][y1], prev = prev, matrix[i][y1]
        smallest = min(smallest, prev)
    
    return smallest, matrix


def solution(rows, columns, queries):
    answer = []
    
    # 기본 행렬 생성
    matrix = []
    num = 1
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(num)
            num += 1
        matrix.append(row)
    
    for query in queries:
        n, matrix = rotate(matrix, query)
        answer.append(n)

    return answer