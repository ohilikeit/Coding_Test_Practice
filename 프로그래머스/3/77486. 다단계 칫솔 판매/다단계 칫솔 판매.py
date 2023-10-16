"""
어느정도 판매가 이루어진 후 누가 얼마만큼의 이득을 가져갔는지
민호 -> center, 8명의 판매원 
모든 판매원은 칫솔의 판매에 의하여 발생하는 이익에서 10%를 계산하여 자신을 조직에 참여시킨 추천인에게 배분하고 나머지 가짐
모든 판매원은 자신이 칫솔판매에서 발생한 이익뿐만아니라 가입시킨 판매워 10%까지 자기 이익
enroll -> 민호를 제외한 조직원 
referral
i번째 이름 
"""

def solution(enroll, referral, seller, amount):
    result = []
    memberRecommender = dict() # 추천인 dict에 넣고
    memberProfit = dict() # 수익금

    for i in range(len(enroll)):
        memberRecommender[enroll[i]] = referral[i]
        memberProfit[enroll[i]] = 0

    #for i in range(len(amount)):
    #    memberProfit[seller[i]] = amount[i]*100

    for i in range(len(seller)):
        cur = seller[i]
        profit = amount[i]*100
        memberProfit[cur] += amount[i]*100
        while memberRecommender[cur] != '-':
            if profit == 0:
                break
            profit = int(0.1*profit)
            memberProfit[cur] -= profit
            memberProfit[memberRecommender[cur]] += profit
            cur = memberRecommender[cur]    
        if memberRecommender[cur] == '-':
            memberProfit[cur] -= int(profit*0.1)
    for member in enroll:
        result.append(memberProfit[member])
    return result




    answer = []
    return answer