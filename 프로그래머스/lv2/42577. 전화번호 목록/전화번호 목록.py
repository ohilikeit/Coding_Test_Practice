def solution(phone_book):
    answer = True
    # 정렬 --> str 안에 숫자들은 말그대로 숫자 순서대로 정렬된다. 
    # ["119", "97674223", "1195524421"] --> ["119", "1195524421", "97674223"]
    phone_book.sort()
    
    # for문이 돌아가면서 앞의 문자가 바로 뒤 문자의 접두사인지를 startswith으로 확인하고
    # 발견하면 바로 False를 뱉어준다! 
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
        
    return answer