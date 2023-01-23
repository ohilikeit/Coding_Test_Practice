from collections import deque
def solution(begin, target, words):
    bfs_stack = deque([(begin, 0)])
    search_level = 0

    while bfs_stack:
        cur_word , search_level = bfs_stack.popleft()  
        for word in words:
            if one_difference(cur_word, word):
                if word == target: return search_level + 1
                bfs_stack.append((word, search_level+1))


    answer = 0
    return answer




def one_difference(word1, word2):
    difference_times = 0
    for char1, char2 in zip(word1,word2):
        if char1 != char2:
            difference_times += 1
    return difference_times == 1 