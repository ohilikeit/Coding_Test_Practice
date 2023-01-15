def solution(numbers, direction):
    answer = []
    if direction == 'right':
        a = numbers.pop()
        numbers.insert(0, a)
    else:
        a = numbers[0]
        del numbers[0]
        numbers.append(a)
    return numbers