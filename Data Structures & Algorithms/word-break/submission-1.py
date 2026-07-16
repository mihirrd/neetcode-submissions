class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1]*(len(s)+1)
        def _dfs(i):
            if i > n: return False
            if i == n: return True
            if dp[i] != -1:
                return dp[i]
            res = False
            for w in wordDict:
                wlen = len(w)
                if i + wlen <= n and w == s[i:i+wlen]:
                    res = res or _dfs(i+wlen)
            dp[i] = res
            return res
        
        return _dfs(0)

        