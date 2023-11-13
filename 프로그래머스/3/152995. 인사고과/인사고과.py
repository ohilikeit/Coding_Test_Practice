def solution(scores):
    wanho, scores = scores[0], scores[1:]
    wanho_wa, wanho_pr = wanho
    threshold_pr = 0
    rank = 1
    for work_attitude, peer_review in sorted(scores, key=lambda s: (-s[0], s[1])):
        if wanho_wa < work_attitude and wanho_pr < peer_review:
            return -1

        if threshold_pr <= peer_review:
            threshold_pr = peer_review

            if wanho_wa + wanho_pr < work_attitude + peer_review:
                rank += 1

    return rank