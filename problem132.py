class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        eh_palindromo = [[False] * n for _ in range(n)]
        cortes = [0] * n
        
        for i in range(n):
            min_cortes = i

            for j in range(i + 1):
                if s[j] == s[i] and (i - j <= 2 or eh_palindromo[j + 1][i - 1]):
                    eh_palindromo[j][i] = True
                    if j == 0:
                        min_cortes = 0
                    else:
                        min_cortes = min(min_cortes, cortes[j - 1] + 1)
                        
            cortes[i] = min_cortes
        
        return cortes[n - 1]
