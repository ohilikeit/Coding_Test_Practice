def solution(a, b):
    lst = ['FRI','SAT','SUN','MON','TUE','WED','THU'] * 2
    days = b
    for i in range(1, a):
        if i in [1,3,5,7,8,10,12]:
            month = 31
        elif i in [4,6,9,11]:
            month = 30
        else:
            month = 29
        days += month
    days = days % 7
    
    return lst[days-1]