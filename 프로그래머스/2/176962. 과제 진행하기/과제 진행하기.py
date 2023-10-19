from collections import deque


def solution(plans):
    def get_time(time):
        hour, minute = int(time[0:2]), int(time[3:5])
        return hour * 60 + minute

    plans = sorted(list(
        map(lambda x: [x[0], get_time(x[1]), int(x[2])], plans)), key=lambda x: x[1])
    answer, wait, now = [], deque([plans[0]]), plans[0][1]

    for i, v in enumerate(plans[1:]):
        next_time = v[1]

        while wait:
            j, t, q = wait.pop()
            if t > now:
                now = t
            lest = now + q

            if lest <= next_time:
                now += q
                answer.append(j)
            else:
                now = next_time
                wait.append([j, t, lest - next_time])
                break

        wait.append(v)

    while wait:
        answer.append(wait.pop()[0])

    return answer