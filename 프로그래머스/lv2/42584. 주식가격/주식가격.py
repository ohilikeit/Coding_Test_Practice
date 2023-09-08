def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            j, _ = stack.pop()
            answer[j] = i - j
        stack.append((i, price))
    
    while stack:
        j, _ = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer
