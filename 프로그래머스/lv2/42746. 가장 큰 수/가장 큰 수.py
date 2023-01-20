def solution(numbers):
    if list(set(numbers)) == [0]:
        return "0"
    answer = ''
    numbers = [(4 * str(i)) for i in numbers]
    numbers.sort(reverse=True, key = lambda x: [x[0],x[1],x[2],x[3]])
    for i in range(len(numbers)):
        answer += numbers[i][:len(numbers[i])//4]  
        
    
    
    return answer