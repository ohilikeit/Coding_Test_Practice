def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1):
        temp = phone_book[i]
        if temp == phone_book[i+1][:len(temp)]:
            answer = False
            break

    return answer