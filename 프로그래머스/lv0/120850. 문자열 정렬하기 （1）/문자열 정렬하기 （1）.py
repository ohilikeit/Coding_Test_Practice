import re

def solution(my_string):
    a = re.sub(r'[a-z]', '', my_string)
    return sorted([int(i) for i in a])