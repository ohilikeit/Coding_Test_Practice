import re

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
        
    if len(new_id) == 0:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
            
    if len(new_id) <= 2:
        idx = new_id[-1]
        while len(new_id) < 3:
            new_id += idx
    
    return new_id