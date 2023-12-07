def palindromo(S):
  n = len(S)
  dp = [[0 for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(i + 1):
      if S[i] == S[j]:
        dp[i][j] = dp[i-1][j-1] + 2
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  return S[0:dp[n-1][n-1]]

S = "ACGT GT CAAAAT CG"

palindromo = palindromo(S)

print(palindromo)
