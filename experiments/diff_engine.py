class DiffEngine:
    def __init__(self, old_text, new_text):
        self.old_lines = old_text.splitlines()
        self.new_lines = new_text.splitlines()
    
    def lcs(self):
        m, n = len(self.old_lines), len(self.new_lines)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.old_lines[i - 1] == self.new_lines[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        result = []
        i, j = m, n
        
        while i > 0 and j > 0:
            if self.old_lines[i - 1] == self.new_lines[j - 1]:
                result.append(("same", self.old_lines[i - 1]))
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                result.append(("removed", self.old_lines[i - 1]))
                i -= 1
            else:
                result.append(("added", self.new_lines[j - 1]))
                j -= 1
        
        while i > 0:
            result.append(("removed", self.old_lines[i - 1]))
            i -= 1
        
        while j > 0:
            result.append(("added", self.new_lines[j - 1]))
            j -= 1
        
        return result[::-1]
    
    def stats(self):
        diff = self.lcs()
        added = sum(1 for op, _ in diff if op == "added")
        removed = sum(1 for op, _ in diff if op == "removed")
        same = sum(1 for op, _ in diff if op == "same")
        
        return {
            "added": added,
            "removed": removed,
            "unchanged": same,
            "total": len(diff)
        }
    
    def unified(self, context=2):
        diff = self.lcs()
        output = []
        
        for op, line in diff:
            if op == "same":
                output.append(f"  {line}")
            elif op == "added":
                output.append(f"+ {line}")
            elif op == "removed":
                output.append(f"- {line}")
        
        return "\n".join(output)

if __name__ == "__main__":
