def diff_lines(old, new):
    old_lines = old.splitlines()
    new_lines = new.splitlines()
    m, n = len(old_lines), len(new_lines)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if old_lines[i-1] == new_lines[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if old_lines[i-1] == new_lines[j-1]:
            result.append((" ", old_lines[i-1]))
            i -= 1; j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            result.append(("-", old_lines[i-1]))
            i -= 1
        else:
            result.append(("+", new_lines[j-1]))
            j -= 1
    while i > 0:
        result.append(("-", old_lines[i-1]))
        i -= 1
    while j > 0:
        result.append(("+", new_lines[j-1]))
        j -= 1
    
    return result[::-1]

def format_diff(old, new):
    return "\n".join(f"{sign} {line}" for sign, line in diff_lines(old, new))
