def solution(players, callings):
    answer = []
    PlayerDict = dict()
    
    for idx, player in enumerate(players):
        PlayerDict[player] = idx
    
    for player in callings:
        # 앞지른 선수 인덱스 뽑아내기 
        idx = PlayerDict.get(player)
        
        # 뒤쳐진 선수 뽑아내기
        looser = players[idx-1]
        
        # 인덱스 수정
        PlayerDict[player] = idx-1
        PlayerDict[looser] = idx
        
        # players에서도 자리 교환
        players[idx] = looser
        players[idx-1] = player

    return players