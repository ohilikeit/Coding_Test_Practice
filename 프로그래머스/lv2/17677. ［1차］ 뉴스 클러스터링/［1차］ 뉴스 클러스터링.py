import re
def cuting(txt):
    lst = []
    for i in range(len(txt)-1):
        if txt[i:i+2].isalpha():
            lst.append(txt[i:i+2])
    return [i.lower() for i in lst]
    
def solution(str1, str2):
    lst1 = cuting(str1)
    lst2 = cuting(str2)
    if not lst1 and not lst2:
        return 65536
    
    one = lst1.copy()
    two = lst2.copy()
    # 교집합
    duplicated = []
    for i in lst1:
        if i in two:
            duplicated.append(i)
            one.remove(i)
            two.remove(i)
    # 합집합
    added = duplicated + one + two
    
    answer = int((len(duplicated) / len(added)) * 65536)
    
    return answer