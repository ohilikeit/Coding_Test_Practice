def solution(alp, cop, problems):
    # The maximum values for alp and cop considering the problem's constraints
    max_alp = max([max(alp, p[0]) for p in problems])
    max_cop = max([max(cop, p[1]) for p in problems])

    # Initialize a 2D array with inf time, +1 to include the max_alp and max_cop in our dp array
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    # Sort the problems by cost in ascending order to use the greedy approach
    problems.sort(key=lambda x: x[-1])

    # Iterate over all possible alp and cop values
    for current_alp in range(alp, max_alp + 1):
        for current_cop in range(cop, max_cop + 1):
            if current_alp > alp:
                # Increase alp by studying, which takes 1 time unit
                dp[current_alp][current_cop] = min(dp[current_alp][current_cop], dp[current_alp - 1][current_cop] + 1)
            if current_cop > cop:
                # Increase cop by studying, which takes 1 time unit
                dp[current_alp][current_cop] = min(dp[current_alp][current_cop], dp[current_alp][current_cop - 1] + 1)

            # Check if solving any problem can lead to a quicker increase in alp or cop
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if current_alp >= alp_req and current_cop >= cop_req:
                    # If we can solve this problem, see if it gives us a quicker way to increase alp or cop
                    new_alp = min(max_alp, current_alp + alp_rwd)
                    new_cop = min(max_cop, current_cop + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[current_alp][current_cop] + cost)

    return dp[max_alp][max_cop]
