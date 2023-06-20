def solution(numbers):
    answer = ''
    if list(set(numbers)) == [0]:
        return '0'
    new_numbers = [4 * str(i) for i in numbers]
    new_numbers.sort(reverse=True, key = lambda x: [x[0], x[1], x[2], x[3]])
    
    for i in new_numbers:
        answer += str(i[:len(i) // 4])
    
    return answer